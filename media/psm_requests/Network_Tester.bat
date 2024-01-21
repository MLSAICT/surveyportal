@echo off

ping -4 -n 1 192.168.2.2 | find "TTL=" >nul
if errorlevel 1 (
    echo DNS Down
) else (
    echo DNS Working
)

ping -4 -n 1 192.168.2.3 | find "TTL=" >nul
if errorlevel 1 (
    echo Fileserver Down
) else (
    echo Fileserver Working
)

ping -4 -n 1 192.168.2.1 | find "TTL=" >nul
if errorlevel 1 (
    echo Gateway Down
) else (
    echo Gateway Working
)

ping -4 -n 1 192.168.2.96 | find "TTL=" >nul
if errorlevel 1 (
    echo LIS Primary Down
) else (
    echo LIS Primary Working
)

ping -4 -n 1 LIS01 | find "TTL=" >nul
if errorlevel 1 (
    echo LIS01 Down
) else (
    echo LIS01 Working
)

ping -4 -n 1 LIS02 | find "TTL=" >nul
if errorlevel 1 (
    echo LIS02 Down
) else (
    echo LIS02 Working
)

ping -4 -n 1 LIS03 | find "TTL=" >nul
if errorlevel 1 (
    echo LIS03 Down
) else (
    echo LIS03 Working
)

ping -4 -n 1 192.168.2.171 | find "TTL=" >nul
if errorlevel 1 (
    echo ProxyServer Down
) else (
    echo ProxyServer Working
)

pause