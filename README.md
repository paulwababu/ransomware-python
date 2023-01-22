# File Encryption Script

This project is a script that encrypts files on your computer for added security. The encryption key is sent via email for safekeeping, and the script can be converted into an executable file for Windows users using Pyinstaller. For Linux and Mac users, the script can be run as is, as long as Python is installed on the computer.
To encrypt all folders, for both windows and mac, head over to my [blog for how to modify the code](https://dev.to/paulwababu)
## Getting Started

### Prerequisites

    - Python 3.8
    - PyAesCrypt library
    - Pyinstaller (for Windows users)

### Installing

    - Clone the repository or download the script files.
    - Install the required libraries by running pip install pyAesCrypt.
    - Edit the script to specify the folders that you wish to encrypt.
    Run the script using python encrypt.py or use pyinstaller to convert it to an executable.

### Usage

The script will encrypt every file in the specified folders, and then move the encrypted files to a new location, with a new file name. The encryption key is sent via email for safekeeping.

For Windows users, you can use Pyinstaller to convert the encryption script into an executable file. This will allow the script to run without the need for Python to be installed on the computer. To convert the script, open the command prompt and navigate to the location of the script. Then, run the command "pyinstaller --onefile encrypt.py"

For decryption, you'll need to run the decryption script and enter the key that was used for encryption. The script will decrypt every file in the specified folders, and then move the decrypted files to a new location, with a new file name.

## Disclaimer

Please be aware that this script is for educational purposes only. The author of this script takes no responsibility for any damage caused by its use. Use at your own risk. It is important to also note that this script encrypts only the files specified in the folder path. It is recommended that a backup copy of your files is kept before running the script.

## License

This project is open source and is licensed under the [MIT License](https://opensource.org/licenses/MIT)
