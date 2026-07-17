# PyInstaller specification for the PhantomBlock Linux executable.
from PyInstaller.utils.hooks import collect_all

datas, binaries, hiddenimports = collect_all("scapy")

analysis = Analysis(
    ["../src/phantomblock/cli.py"],
    pathex=["../src"],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports + ["uvicorn.logging", "uvicorn.loops.auto", "uvicorn.protocols.http.auto"],
    noarchive=False,
)
pyz = PYZ(analysis.pure)
exe = EXE(
    pyz,
    analysis.scripts,
    analysis.binaries,
    analysis.datas,
    [],
    name="phantomblock",
    console=True,
    strip=True,
    upx=False,
)
