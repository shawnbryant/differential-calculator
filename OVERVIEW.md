# Differential Setup Calculator — Overview

A browser-based tool for completing a full first-time differential rebuild setup.  
Open `index.html` in any browser. No internet or installation required.

---

## How to Open

Double-click **`launch.command`** — opens the calculator in your default browser.  
Or open `index.html` directly from Finder.

---

## The 5 Steps (in order)

| Step | What You're Doing | Tool Needed |
|------|-------------------|-------------|
| **1 — Pinion Depth** | Find how much shim the pinion needs to sit at the correct distance from the axle centerline | Depth gauge, outside calipers |
| **2 — Pinion Preload** | Set the pinion bearing load by tightening the pinion nut and reading rotating torque | In-lb torque wrench |
| **3 — Backlash** | Distribute the carrier shim stack side-to-side to hit the backlash target | Dial indicator |
| **4 — Runout** | Check that the ring gear isn't wobbling excessively once installed | Dial indicator |
| **5 — Pattern Check** | Apply gear marking compound and read the contact pattern as a final verification | Gear blue / marking compound |

---

## Input Fields — Quick Reference

### Header (fill these first)
| Field | What it is | Where to get it |
|-------|-----------|-----------------|
| Differential / Axle | Your specific axle model | Axle ID tag on housing, or door jamb sticker |
| Gear Ratio | Ring/pinion ratio (e.g. 4.10) | Axle tag, door jamb, or count teeth |
| Bearing Condition | New or reused pinion bearings | Based on what you installed |
| Vehicle / Notes | Free text for your reference | Anything — prints on the sheet |

### Step 1 — Pinion Depth
| Field | What it is | How to measure |
|-------|-----------|----------------|
| Face to Race | Diff housing face → top of carrier bearing race bore | Depth micrometer on housing face |
| Race OD | Outside diameter of the carrier bearing race | Outside calipers across the race |
| Face to Pinion | Diff housing face → front face of pinion head | Depth gauge into housing |
| Pinion Etched Target Marking | Manufacturer's desired checking distance — stamped on pinion head | Read the stamp on the pinion face |
| Housing Internal Width | Inside span between the two carrier bearing bores | Inside micrometer in housing |
| Carrier + Races Width | Carrier assembly width with races, no shims | Outside micrometer across races |
| Desired Carrier Preload | How much interference you want on the carrier bearings | Typically 0.008" — check service manual |

### Step 2 — Pinion Preload
| Field | What it is | How to measure |
|-------|-----------|----------------|
| Measured Rotating Preload | Continuous torque to spin the pinion (in-lb) | In-lb torque wrench on pinion nut — **no ring gear, no seal** |

### Step 3 — Backlash
| Field | What it is | How to measure |
|-------|-----------|----------------|
| Ring Gear Side | Which side the ring gear is on (from pinion end) | Look at the open diff — usually driver's side |
| Ring Gear Side Shims | Current shim thickness on ring gear side | Start at 50% of total; adjust after measuring |
| Measured Backlash | Lash between ring gear and pinion teeth | Dial indicator on ring gear face, pinion held still |
| Target Backlash | Desired backlash spec | Gear set instruction sheet or service manual |

### Step 4 — Runout
| Field | What it is | How to measure |
|-------|-----------|----------------|
| Ring Gear TIR | Total wobble of the ring gear over one revolution | Dial indicator on ring gear back face — rotate one full turn |

---

## Key Formulas

```
Axle Centerline    = Face to Race + (Race OD / 2)
Checking Distance  = Face to Pinion − Axle Centerline
Shim Adjustment    = Checking Distance − Pinion Etched Target
Total Carrier Shim = (Housing Width − Carrier Width) + Carrier Preload
```

**Shim adjustment rule:**
- Result is **positive** → ADD shim (pinion needs to go deeper)
- Result is **negative** → REMOVE shim (pinion is too deep)

**Backlash rule (moving shims side-to-side):**
- Too much backlash → move shim TO the ring gear side
- Too little backlash → move shim AWAY from the ring gear side

---

## Pattern Guide (Step 5)

| Pattern Location | Meaning | Fix |
|-----------------|---------|-----|
| Centered on tooth | Correct | Nothing — assemble |
| Toward Toe (narrow end) | Pinion too deep | Remove pinion shim |
| Toward Heel (wide end) | Pinion too shallow | Add pinion shim |
| Drive/Coast split top-to-bottom | Backlash issue | Adjust shims side-to-side |

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `index.html` | The calculator — open this in any browser |
| `launch.command` | Double-click shortcut to open in browser |
| `differential_calculator.py` | Python reference/backend logic |
| `test_calculator.py` | Test suite for the Python logic |
| `OVERVIEW.md` | This file |
| `setup.command` | First-time setup / permission fixer |
