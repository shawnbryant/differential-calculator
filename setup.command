#!/bin/bash
# ─── Differential Calculator — Setup / Launcher ───────────────────────────────
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

echo ""
echo "  ┌─────────────────────────────────────────────┐"
echo "  │   Differential Setup Calculator             │"
echo "  │   First-time setup & launcher               │"
echo "  └─────────────────────────────────────────────┘"
echo ""

# Fix execute permissions on launch files
chmod +x "$DIR/launch.command" 2>/dev/null
chmod +x "$DIR/setup.command"  2>/dev/null
echo "  ✓ Permissions set on launch files"

# Check that index.html exists
if [ ! -f "$DIR/index.html" ]; then
    echo ""
    echo "  ✗ ERROR: index.html not found in $DIR"
    echo "    Make sure all files are in the same folder."
    echo ""
    read -p "  Press Enter to close..."
    exit 1
fi
echo "  ✓ index.html found"

# Optional: check Python is available (for differential_calculator.py)
if command -v python3 &>/dev/null; then
    echo "  ✓ Python 3 found: $(python3 --version 2>&1)"
else
    echo "  ⚠  Python 3 not found — the HTML calculator still works without it"
fi

echo ""
echo "  ─────────────────────────────────────────────"
echo "  Quick reference:"
echo ""
echo "  Open calculator :  double-click  launch.command"
echo "  Overview / docs  :  open OVERVIEW.md in any text editor"
echo "  Tutorial         :  click 'Start Tutorial' inside the calculator"
echo ""
echo "  5-Step Process:"
echo "    1. Pinion Depth   — shim the pinion to the correct depth"
echo "    2. Pinion Preload — set pinion bearing preload (in-lb)"
echo "    3. Backlash       — distribute carrier shims for correct backlash"
echo "    4. Runout         — verify ring gear runout < 0.003\""
echo "    5. Pattern        — check gear contact pattern with marking compound"
echo ""
echo "  Key formula:  Shim Adj = Checking Distance − Pinion Etched Marking"
echo "    Positive result → ADD shim"
echo "    Negative result → REMOVE shim"
echo "  ─────────────────────────────────────────────"
echo ""

# Open the calculator
echo "  Opening calculator..."
open "$DIR/index.html"

echo ""
read -p "  Press Enter to close this window..."
