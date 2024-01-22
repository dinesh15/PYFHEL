
# README

## Introduction

This document provides instructions for setting up Pyfhel, a Python library for Homomorphic Encryption (HE). Pyfhel allows performing arithmetic operations on encrypted data without needing to decrypt it first, enabling privacy-preserving computations.

## Prerequisites

Before installing Pyfhel, ensure you have Python 3.6 or newer installed on your system. Pyfhel is compatible with Linux, macOS, and Windows operating systems. Additionally, some dependencies may require a C++ compiler.

## Installation

### Step 1: Install Pyfhel

Pyfhel can be installed directly from PyPI using pip. Open your terminal or command prompt and run the following command:

```bash
pip install pyfhel
```

This command downloads Pyfhel and its Python dependencies. For some systems, compiling from source might be necessary, which could require additional tools like CMake and a C++ compiler.

### Step 2: Verify Installation

To verify that Pyfhel has been installed correctly, try importing it in a Python interactive session or script:

```python
from Pyfhel import Pyfhel
print("Pyfhel imported successfully!")
```

If you see the message "Pyfhel imported successfully!" without any errors, the installation is complete.

## Basic Usage

### Initializing Pyfhel

Before performing any encrypted operations, initialize Pyfhel and generate the necessary keys:

```python
HE = Pyfhel()
HE.contextGen(p=65537, m=4096, base=2, sec=128, flagBatching=True)
HE.keyGen()
HE.relinKeyGen()
```

This code snippet creates a Pyfhel object, generates a context with specified parameters, and generates the public and secret keys needed for encryption and decryption.

### Encrypting and Decrypting Data

Here's a simple example of encrypting and decrypting an integer:

```python
# Encrypt an integer
encrypted_integer = HE.encryptInt(42)

# Decrypt the integer
decrypted_integer = HE.decryptInt(encrypted_integer)
print(f"Decrypted integer: {decrypted_integer}")
```

### Performing Encrypted Operations

Pyfhel supports various arithmetic operations on encrypted data. Here's an example of adding two encrypted integers:

```python
# Encrypt two integers
enc_int1 = HE.encryptInt(10)
enc_int2 = HE.encryptInt(32)

# Perform encrypted addition
enc_sum = enc_int1 + enc_int2

# Decrypt the result
decrypted_sum = HE.decryptInt(enc_sum)
print(f"Decrypted sum: {decrypted_sum}")
```

## Advanced Features

Pyfhel also supports more advanced features, such as working with real numbers using the CKKS scheme, batching for vectorized operations, and more. Refer to the official Pyfhel documentation for detailed information on these features.

## Conclusion

Pyfhel offers a powerful toolkit for privacy-preserving computations through homomorphic encryption. By following the setup instructions and exploring the basic usage examples provided in this document, you can start integrating encrypted operations into your Python projects.

For more detailed information, troubleshooting, and advanced usage examples, please refer to the [official Pyfhel GitHub repository](https://github.com/ibarrond/Pyfhel) and documentation.
