use pyo3::prelude::*;
use pyo3::types::PyBytes;

use base64::engine::{general_purpose, Engine as _};
use data_encoding::BASE32;

fn printable_ascii(buf: &[u8]) -> bool {
    buf.iter().all(|&b| b.is_ascii_graphic() || b == b' ')
}

fn to_py_string(py: Python<'_>, bytes: &[u8]) -> PyObject {
    PyBytes::new_bound(py, bytes).into_py(py)
}

#[pyfunction]
fn decode_base64(py: Python<'_>, raw: &[u8]) -> PyResult<Option<PyObject>> {
    match general_purpose::STANDARD_NO_PAD.decode(raw) {
        Ok(decoded) if printable_ascii(&decoded) => {
            Ok(Some(to_py_string(py, &decoded)))
        }
        _ => Ok(None),
    }
}

#[pyfunction]
fn decode_base32(py: Python<'_>, raw: &[u8]) -> PyResult<Option<PyObject>> {
    match BASE32.decode(raw) {
        Ok(decoded) if printable_ascii(&decoded) => {
            Ok(Some(to_py_string(py, &decoded)))
        }
        _ => Ok(None),
    }
}

#[pyfunction]
fn decode_base85(py: Python<'_>, raw: &[u8]) -> PyResult<Option<PyObject>> {
    // ASCII85 implementation
    match base64::engine::general_purpose::STANDARD.decode(raw) {  // Temporary fallback to base64
        Ok(decoded) if printable_ascii(&decoded) => {
            Ok(Some(to_py_string(py, &decoded)))
        }
        _ => Ok(None),
    }
}

#[pymodule]
fn smarthunter_fast(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(decode_base64, m)?)?;
    m.add_function(wrap_pyfunction!(decode_base32, m)?)?;
    m.add_function(wrap_pyfunction!(decode_base85, m)?)?;
    Ok(())
} 