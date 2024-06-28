import os
import re
import subprocess
import requests
import colorama
from colorama import Fore, Style

colorama.init()

def install_packages():
    """Install required packages."""
    packages = ['requests', 'colorama']
    for package in packages:
        subprocess.run(['pip', 'install', '-q', package])

def clear_console():
    """Clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def prompt_language():
    """Prompt the user to set language."""
    print(Fore.YELLOW + "\nPYTHON EXE AUTOMATIC COMPILER Ver 2.0\n")
    print("© 2024. Diddmstjr Inc. All rights reserved.\n" + Style.RESET_ALL)
    while True:
        language = input(Fore.GREEN + "Please Set Language(Korean/English): " + Style.RESET_ALL).strip().lower()
        if language in ['korean', 'english']:
            return language
        print(Fore.RED + "Invalid input. Please type 'Korean' or 'English'." + Style.RESET_ALL)

def main():
    """Main function to drive the script."""
    install_packages()
    clear_console()
    language = prompt_language()

    if language == 'korean':
        clear_console()
        korean_version()
    else:
        english_version()

def korean_version():
    gui_version = input(Fore.GREEN + "->" + Style.RESET_ALL + " 터미널을 활용한 프로그램, 일반 사용자를 위한 GUI 버전(1, 2): ").strip()
    language_count = input(Fore.GREEN + "->" + Style.RESET_ALL + " 변환할 언어의 개수를 입력하여 주십시오: ").strip()
    extensions = input(Fore.GREEN + "->" + Style.RESET_ALL + " 윈도우용 실행 파일로 변환할 프로그램 언어 확장자명을 입력하여 주십시오 (2개 이상일 경우 띄어쓰기로 명시하여 주십시오): ").strip()
    app_name = input(Fore.GREEN + "->" + Style.RESET_ALL + " 어플리케이션 이름을 입력하여 주십시오: ").strip()
    app_version = input(Fore.GREEN + "->" + Style.RESET_ALL + " 어플리케이션 버전을 입력하여 주십시오: ").strip()
    author_name = input(Fore.GREEN + "->" + Style.RESET_ALL + " 저작권자의 이름을 입력하여 주십시오: ").strip()
    author_website = input(Fore.GREEN + "->" + Style.RESET_ALL + " 저작권자의 사이트를 입력하여 주십시오: ").strip()
    process_files = input(Fore.GREEN + "->" + Style.RESET_ALL + " 실행할 파일명을 띄어쓰기로 구분하여 입력하여 주십시오: " + Style.RESET_ALL).strip()

    try:
        if int(language_count) != len(extensions.split()):
            raise ValueError("\nTyped extension amount and language amount doesn't coincide\n")
    except ValueError as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)
        return

    iss_content = generate_iss_content(app_name, app_version, author_name, author_website, process_files, extensions)
    with open('setting.iss', 'w') as file:
        file.write(iss_content)
    
    print(Fore.GREEN + "\n✔ ISS 파일이 성공적으로 생성되었습니다 ✔" + Style.RESET_ALL)
    convert_iss_to_exe()

def english_version():
    """English version of the program."""
    gui_version = input(Fore.GREEN + "-> Console usage program, Non-Console Usage program -> GUI user version(1, 2): " + Style.RESET_ALL).strip()
    language_count = input(Fore.GREEN + "-> Please type your Program Language amount to convert: " + Style.RESET_ALL).strip()
    extensions = input(Fore.GREEN + "-> Please type your Program Language extension name to convert as Windows program(exe) (If extension name is more than 2, please envince as space.): " + Style.RESET_ALL).strip()
    app_name = input(Fore.GREEN + "-> Please type application name: " + Style.RESET_ALL).strip()
    app_version = input(Fore.GREEN + "-> Please type application version: " + Style.RESET_ALL).strip()
    author_name = input(Fore.GREEN + "-> Please type copywriter name: " + Style.RESET_ALL).strip()
    author_website = input(Fore.GREEN + "-> Please type copywriter homepage: " + Style.RESET_ALL).strip()
    process_files = input(Fore.GREEN + "-> Please type process file name envince as space: " + Style.RESET_ALL).strip()
    try:
        if int(language_count) != len(extensions.split()):
            raise ValueError("Typed extension amount and language amount doesn't coincide")
    except ValueError as e:
        print(Fore.RED + str(e) + Style.RESET_ALL)
        return
    iss_content = generate_iss_content(app_name, app_version, author_name, author_website, process_files, extensions)
    with open('setting.iss', 'w') as file:
        file.write(iss_content)
    print(Fore.GREEN + "\n✔ ISS File Successfully Created ✔" + Style.RESET_ALL)
    convert_iss_to_exe()

def generate_iss_content(app_name, app_version, author_name, author_website, process_files, extensions):
    """Generate the content for the ISS file."""
    return f"""[Setup]
AppId={{D4268BF5-990D-48EE-97A7-88473C09CE36}}
AppName={app_name}
AppVersion={app_version}
AppPublisher={author_name}
AppPublisherURL={author_website}
DefaultDirName={{autopf}}\\{app_name}
ChangesAssociations=yes
DisableProgramGroupPage=yes
OutputBaseFilename={app_name}
SetupIconFile=.\asset\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{{cm:CreateDesktopIcon}}"; GroupDescription: "{{cm:AdditionalIcons}}"; Flags: unchecked

[Files]
Source: ".\\module\\{process_files}"; DestDir: "{{app}}"; Flags: ignoreversion

[Icons]
Name: "{{autoprograms}}\\{app_name}"; Filename: "{{app}}\\{process_files}"
Name: "{{autodesktop}}\\{app_name}"; Filename: "{{app}}\\{process_files}"; Tasks: desktopicon

[Run]
Filename: "{{app}}\\{process_files}"; Description: "{{cm:LaunchProgram,{app_name}}}"; Flags: nowait postinstall skipifsilent
    """

def convert_iss_to_exe():
    """Convert ISS file to EXE using Inno Setup."""
    iss_file_path = './setting.iss'
    iscc_path = 'C:\\Program Files (x86)\\Inno Setup 6\\ISCC.exe'

    try:
        subprocess.run([iscc_path, iss_file_path, '/VERYSILENT', '/NORESTART'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(Fore.GREEN + "\n✔ EXE 파일이 성공적으로 생성되었습니다 ('./Output/') ✔" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error: {str(e)}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()