@echo off
:begin
@echo off&amp;color 0A
cls
echo,
echo ��ѡ��Ҫ�����ϵͳ������
echo,
echo 1. setting_package_name
echo 2. windows_amd64
echo 3. windows_i386
echo 4. linux_amd64
echo 5. linux_i386
echo 6. darwin_amd64
echo 7. darwin_i386
echo 0. quit
echo,


set /p c=��ѡ��:
if %c% equ 1 (
set /p GOBIN=ָ���������������:
)

setlocal enabledelayedexpansion
if %c% equ 2 (
echo ����Windows�汾64λ
SET CGO_ENABLED=0
SET GOOS=windows
SET GOARCH=amd64
go build -o %GOBIN%_windows_amd64.exe
)

if %c% equ 3 (
echo ����Windows�汾32λ
SET CGO_ENABLED=0
SET GOOS=windows
SET GOARCH=386
go build -o %GOBIN%_windows_i386.exe
)

if %c% equ 4 (
echo ����Linux�汾64λ
SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=amd64
go build -o %GOBIN%_linux_amd64
)

if %c% equ 5 (
echo ����Linux�汾32λ
SET CGO_ENABLED=0
SET GOOS=linux
SET GOARCH=386
go build -o %GOBIN%_linux_i386
)

if %c% equ 6 (
echo ����darwin�汾64λ
SET CGO_ENABLED=0
SET GOOS=darwin
SET GOARCH=amd64
go build -o %GOBIN%_darwin_amd64
)

if %c% equ 7 (
echo ����darwin�汾32λ
SET CGO_ENABLED=0
SET GOOS=darwin
SET GOARCH=386
go build -o %GOBIN%_darwin_i386
)

if %c% equ 0 (
echo Quit
exit
)

goto begin
*/;