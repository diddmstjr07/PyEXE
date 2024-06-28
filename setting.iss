[Setup]
AppId={D4268BF5-990D-48EE-97A7-88473C09CE36}
AppName=diddmstjr
AppVersion=1.0
AppPublisher=diddmstjr
AppPublisherURL=https://anoasksite
DefaultDirName={autopf}\diddmstjr
ChangesAssociations=yes
DisableProgramGroupPage=yes
OutputBaseFilename=diddmstjr
SetupIconFile=.sset\icon.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: ".\module\main.pyw main.dll"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{autoprograms}\diddmstjr"; Filename: "{app}\main.pyw main.dll"
Name: "{autodesktop}\diddmstjr"; Filename: "{app}\main.pyw main.dll"; Tasks: desktopicon

[Run]
Filename: "{app}\main.pyw main.dll"; Description: "{cm:LaunchProgram,diddmstjr}"; Flags: nowait postinstall skipifsilent
    