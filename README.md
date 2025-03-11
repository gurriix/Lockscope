# Lockscope

This repository contains an educational ransomware project developed in phases, ranging from simple to complex.

## Project Description

This project aims to demonstrate the development of ransomware malware through progressively more sophisticated phases. It is intended for educational purposes only, to understand the mechanisms and complexities of ransomware.

## Phases

### Phase 1: Basic RSA Encryption

-   **Key Generation:** Generates a static 2048-bit RSA asymmetric key.
-   **Encryption:** Encrypts a single file of a specific extension within a designated folder.
-   **Decryption:** The decryption key is stored in a file in the same directory as the ransomware. Simple file search allows for easy decryption.

### Phase 2: Static AES Encryption

-   **Key Generation:** Generates a static 256-bit AES symmetric key.
-   **Encryption:** Encrypts multiple files with various extensions within a specific folder.
-   **Decryption:** The decryption key is stored in a Base64-encoded file in the ransomware's directory. Requires Base64 decoding before decryption.

### Phase 3: Dynamic AES Encryption with Server Communication

-   **Key Generation:** Generates a unique, random 256-bit AES symmetric key for each execution.
-   **Encryption:** Encrypts files in selected system folders with various extensions.
-   **Key Transmission:** The encryption key is sent to a remote server via socket connection.
-   **Decryption:** Requires the attacker to send the decryption key from the server to the victim's machine for immediate decryption.

### Phase 4: Combined RSA and AES Encryption with Server Storage

-   **Key Generation:** Generates both a 256-bit AES symmetric key and a 2048-bit RSA asymmetric key. The AES key is then encrypted with the RSA public key.
-   **Encryption:** Encrypts files in the user's main directory, covering a wide range of file extensions.
-   **Key Transmission:** Both the encrypted AES key and the RSA private key are sent to and stored on a remote server via socket connection.
-   **Decryption:** Requires the attacker to send both keys from the server to the victim's machine. The AES key is decrypted using the RSA private key, followed by file decryption using the AES key.

### Phase 5: Combined RSA and AES Encryption with Dropbox Storage

-   **Key Generation:** Generates both a 256-bit AES symmetric key and a 2048-bit RSA asymmetric key. The AES key is then encrypted with the RSA public key.
-   **Encryption:** Encrypts files in the user's main directory, covering a wide range of file extensions. The resulting AES key, encrypted using the RSA public key, is stored inside a Dropbox folder, instead of being sent directly to the attacker.
-   **Key Transmission:** Both keys are uploaded to a Dropbox folder, monitored by the attacker's server, which then downloads and deletes them.
-   **Decryption:** Requires the attacker to upload both keys to the Dropbox folder. The victim's machine detects the keys and initiates the decryption process. The AES key is decrypted using the RSA private key, followed by file decryption using the AES key.

## Disclaimer

This project is for educational purposes only. Do not use this code for any malicious activities. The developers are not responsible for any misuse of this code.
