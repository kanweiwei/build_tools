1. Necessary repositories:
    - build_tools
    - core
    - desktop-apps
    - desktop-sdk
    - dictionaries
    - document-templates
    - sdkjs
    - web-apps
2. Install softwares as follow:
    - Qt 5.8
    - Visual Studio Community 2015
    - Windows SDK 10 (10.0.20348)
    - Adoptopenjdk 8
    - nodejs
    - grunt
    - python2
    - python3
    - git
    - TortoiseSVN
    - Strawberry Perl
    - 7z

3. Setting environment variables
    - DEPOT_TOOLS_WIN_TOOLCHAIN=0
    - GYP_MSVS_VERSION=2015
    - GYP_CHROMIUM_NO_ACTION=0
    - Add Windows Kits 10 bin dir (such as C:\Program Files (x86)\Windows Kits\10\bin\10.0.20348.0\x64) to PATH variable

4. If the Windows Operating System is set with Chinese language:

    1. DesktopEditors\core\ASCOfficePPTFile\PPTFormatLib\PPTXWriter\TxBodyConverter.cpp need to be saved with encoding "UTF-8 with BOM"
    2. DesktopEditors\desktop-apps\win-linux\src\clangater.cpp need to be saved with encoding "UTF-8 with BOM"

5. Compiled app package is in build_tools/out/win_64/onlyoffice/DesktopEditors

6. Add the DesktopEditors/converter path to the PATH environment variable

7. Run Desktop Editors using the DesktopEditors.exe file.