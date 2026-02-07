# HONKED SECURITY - CAPPIAVI v1.5

## Project Overview

**HONKED Security** is an advanced web-based security monitoring and IP tracking application developed by **Cappiavi** and **Khert Garde**. This project combines a Python Flask backend with a modern web-based control panel interface to monitor and track incoming connections with real-time geolocation mapping and hit logging.

The application utilizes **ngrok** to create secure tunnels and expose a Flask web server to the internet, allowing remote monitoring of captured traffic and IP information. It features a sophisticated control panel with:
- Real-time geolocation mapping using Leaflet
- Live terminal logging and system status updates
- Multi-key failover mechanism for cluster connectivity
- Hit counter and visitor tracking
- Matrix-style visual alerts on visitor pages
- **Note**: Audio notifications only available in development mode (source code version)

---

## Key Features

### 1. **Real-Time IP & Geolocation Tracking**
   - Captures visitor IP addresses and geolocation data using the IP-API service
   - Provides real-time mapping of visitor locations on an interactive Leaflet map
   - Displays city, country, latitude, and longitude information

### 2. **Secure Tunnel Management**
   - Integrates with **ngrok** to create public URLs for the Flask server
   - Implements failover mechanism with multiple cluster keys
   - Automatic reconnection on key failure
   - Dynamic URL management and sharing capabilities

### 3. **Web-Based Control Panel**
   - Built with HTML, CSS, and JavaScript
   - Features split layout: control sidebar + main map/terminal view
   - Real-time terminal output for system logs and alerts
   - Status monitoring and system statistics

### 4. **Interactive Visitor Pages**
   - Matrix-style visual alert pages ("YOU GOT HONKED")
   - Canvas-based animated backgrounds with real-time rendering
   - Responsive design with bright, attention-grabbing visual alerts
   - **Audio Support**: Only available in development mode with source code (not in compiled `.exe`)

### 5. **Multi-Thread Support**
   - Asynchronous operation of Flask server and tunnel management
   - Background threading for non-blocking operations
   - Seamless UI updates via JavaScript evaluation

---

## Complete Setup Guide: Start to Finish

### Phase 1: System Prerequisites Check

Before beginning installation, verify your system meets all requirements:

#### Step 1.1: Verify Windows Version
1. Right-click **This PC** on Desktop
2. Select **Properties**
3. Look for **OS Build** - Should show Windows 10 or Windows 11
4. Verify you have **64-bit version** (look for x64 in System info)

**What to Look For:**
- Windows 10 Build 1909 or later OR Windows 11
- System Type: x64-based processor
- RAM: At least 4GB (2GB minimum, though not recommended)

#### Step 1.2: Check Internet Connection
- Open your web browser
- Navigate to `https://whatismyip.com/`
- Confirm you receive your IP address and location
- **This is required** - The application needs internet access to function

#### Step 1.3: Verify Disk Space
1. Right-click **C: Drive** (or your primary drive)
2. Select **Properties**
3. Check available space
4. **Requirement**: Minimum 300MB free space (recommended 1GB+)

---

### Phase 2: Python Installation (If Not Already Installed)

#### Step 2.1: Check if Python is Installed
1. Press **Windows Key + R**
2. Type: `cmd` and press Enter
3. In Command Prompt, type:
   ```cmd
   python --version
   ```
4. If you see a version number (e.g., "Python 3.11.5"), proceed to Phase 3
5. If you see "python is not recognized", continue with Step 2.2

#### Step 2.2: Download Python
1. Open your browser
2. Go to **https://www.python.org/downloads/**
3. Click the large yellow button labeled **"Download Python 3.11.x"** (or latest 3.7+)
4. Save the installer to your Downloads folder

#### Step 2.3: Install Python
1. Open your Downloads folder
2. Double-click **python-3.11.x-amd64.exe** (or the version you downloaded)
3. **IMPORTANT**: Check the box that says **"Add Python 3.11 to PATH"**
4. Click **Install Now**
5. Wait for installation to complete (may take 2-3 minutes)
6. Click **Close**

#### Step 2.4: Verify Python Installation
1. Press **Windows Key + R**
2. Type: `cmd` and press Enter
3. Type:
   ```cmd
   python --version
   ```
4. You should see something like "Python 3.11.5" (the exact version may differ)
5. Type:
   ```cmd
   pip --version
   ```
6. You should see a version number with a path

**✓ If you see version numbers for both, Python is correctly installed.**

---

### Phase 3: Required Libraries & Packages Installation

#### Important: Understanding the Dependencies

The following libraries are **REQUIRED** before running HONKED Security:

| Library | Version | Purpose | Why Required |
|---------|---------|---------|--------------|
| **pywebview** | 5.0+ | Native GUI window | Creates the desktop control panel interface |
| **requests** | 2.28.0+ | HTTP client library | Communicates with IP-API and ngrok APIs |
| **flask** | 2.2.0+ | Web framework | Runs the backend web server for visitor tracking |
| **pyngrok** | 7.0.0+ | ngrok Python wrapper | Manages tunnel creation and failover |
| **pyperclip** | 1.8.2+ | Clipboard utility | Allows 1-click URL copying for sharing |

#### Step 3.1: Open Command Prompt (Admin)
1. Press **Windows Key**
2. Type: **cmd**
3. Right-click on **Command Prompt**
4. Select **"Run as administrator"**
5. Click **Yes** when prompted

#### Step 3.2: Install All Dependencies (One Command)
Copy and paste this entire command into Command Prompt:

```cmd
pip install --upgrade pip setuptools wheel
```

Wait for completion (you'll see "Successfully installed" messages), then run:

```cmd
pip install pywebview requests flask pyngrok pyperclip
```

**Expected Output:**
```
Collecting pywebview
  Downloading pywebview-5.x.x-...-win_amd64.whl
...
Successfully installed pywebview requests flask pyngrok pyperclip
```

#### Step 3.3: Verify All Packages Installed
Run each of these commands one by one:

```cmd
pip show pywebview
pip show requests
pip show flask
pip show pyngrok
pip show pyperclip
```

Each command should display information about the package. If you see "WARNING: Package X not found", that package failed to install. Run the installation command again.

#### Step 3.4: Alternative - Install via Requirements File (If Available)
If you have a `requirements.txt` file:

1. Open Command Prompt (Admin)
2. Navigate to the folder containing `requirements.txt`:
   ```cmd
   cd C:\path\to\requirements\location
   ```
3. Run:
   ```cmd
   pip install -r requirements.txt
   ```

---

### Phase 4: Preparing ngrok Configuration

#### Step 4.1: Understanding ngrok Cluster Keys
The application uses **ngrok cluster keys** for tunnel creation. These are authentication tokens specific to your ngrok account.

The application contains 3 default cluster keys:
- `39IqyiGfAVlXGoEbC8cCAATxhrr_6aQAdPFU6tSCowhvS5JTK`
- `39J3nGR7GqUf8upt9WD0a1oBXd3_4GYhm6ZHkA3dbhewTvrH5`
- `39J43P5sSGaLaTnDlmPbBvTMKMp_5zipPsrY7AXusMUeBDJ5K`

**Important**: If these keys are invalid or expired, you'll need to update them in the application source code (HONKSEC.py).

#### Step 4.2: Verify ngrok Access (Optional but Recommended)
1. Visit **https://ngrok.com** in your browser
2. Create a free account (or use existing)
3. Go to your **Dashboard**
4. Copy your **Auth Token** from the dashboard
5. Keep this token safe - you may need it if the default keys fail

#### Step 4.3: Firewall Configuration
Before running the application, configure Windows Firewall:

1. Press **Windows Key**
2. Type: **Windows Defender Firewall**
3. Click **"Allow an app through firewall"**
4. Click **"Change settings"**
5. If you see Python listed:
   - Check both **Private** and **Public** boxes next to Python
6. Click **OK**

---

## Installation & Execution Guide

## Complete Installer Setup Instructions

### Phase 5: Running the Installer (RECOMMENDED METHOD)

#### Step 5.1: Locate the Installer
1. Navigate to: `C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\FINAL\HONKED SEC APP\Output\`
2. You should see: **HONKED SECURITY - CAPPIAVI v1.5.exe**
3. Right-click on it and select **"Run as administrator"**
4. Click **"Yes"** when Windows asks for permission

#### Step 5.2: Follow the Installation Wizard
1. **Welcome Screen**: Click **"Next >"**
2. **Select Installation Folder**:
   - Default location: `C:\Program Files\HONKED_SECURITY BY CAPPIAVI`
   - You can change this if desired
   - Click **"Next >"**

3. **Select Start Menu Folder**:
   - Default: HONKED_SECURITY BY CAPPIAVI
   - Click **"Next >"**

4. **Select Additional Tasks**:
   - **Check**: "Create a desktop icon" (Optional but recommended)
   - Click **"Next >"**

5. **Ready to Install**:
   - Review the installation location
   - Click **"Install"**
   - Wait for progress bar to complete (1-2 minutes)

6. **Installation Complete**:
   - **Check**: "Launch HONKED_SECURITY BY CAPPIAVI" if you want to start immediately
   - Click **"Finish"**

#### Step 5.3: Verify Installation Success
1. Press **Windows Key**
2. Type: **HONKED_SECURITY BY CAPPIAVI**
3. You should see the application in search results
4. Check your Desktop - you should see a shortcut icon

---

### Phase 6: First-Run Setup & Configuration

#### Step 6.1: Launch the Application
**Method 1** (Easiest):
- Double-click the Desktop shortcut labeled **"HONKED_SECURITY BY CAPPIAVI"**

**Method 2** (Via Start Menu):
1. Click the Start button (Windows key)
2. Type: **HONKED_SECURITY**
3. Click the result

**Method 3** (Via Command Line):
1. Open Command Prompt
2. Type:
   ```cmd
   python C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\Python End\Honked\HONKSEC.py
   ```

#### Step 6.2: Understand the Control Panel Interface

When the application launches, you'll see:

**Left Sidebar (Control Panel):**
- **Status Indicator**: Green = Online, Red = Offline
- **Boot Failover Button**: Initializes ngrok tunnels
- **Copy Link Button**: Copies the tunnel URL
- **Toggle Status Button**: Activates/Deactivates victim page
- **Trace IP Button**: Manual IP geolocation lookup
- **Shutdown Button** (Red): Closes the application

**Main Area (Right Side):**
- **Top Half**: Interactive Leaflet map showing visitor locations
- **Bottom Half**: Terminal-style log showing all events and hits

#### Step 6.3: Initialize ngrok Tunnels
1. Look at the left panel
2. Locate the **"Boot Failover"** button
3. Click it
4. You should see:
   - Status message: "[SYSTEM] Uplink 01 Online."
   - A URL displayed in the status area (e.g., `https://abc123.ngrok.io`)
   - The status indicator light turns green

**What's Happening:**
- The application is connecting to ngrok servers
- A public tunnel is being created that exposes your local Flask server
- This URL will route to `http://localhost:5000` on your machine
- The URL remains active as long as the application is running

#### Step 6.4: Copy the Tunnel URL
1. Once the URL appears, click the **"Copy Link"** button
2. The URL is now in your clipboard
3. Paste it into a browser to test: **Ctrl+V**
4. You should see the victim page with "YOU GOT HONKED" message

#### Step 6.5: Understanding the Victim Page
When someone (or you) visits the tunnel URL:
1. They see a Matrix-style animated page saying "YOU GOT HONKED"
2. **Note on Audio**: Audio is not available in the installed `.exe` version (see "AUDIO LIMITATIONS" section)
3. In your control panel:
   - Terminal shows: "[!] HIT DETECTED: [IP] | [City]"
   - Map updates with visitor's location
   - Hit counter increments

---

### Phase 7: Advanced Configuration (Optional)

#### Step 7.1: Updating ngrok Cluster Keys
If the default keys expire:

1. Navigate to: `C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\Python End\Honked\`
2. Right-click **HONKSEC.py**, select **"Open with"** > **Notepad**
3. Find this section (around line 10):
   ```python
   CLUSTER_KEYS = [
       "39IqyiGfAVlXGoEbC8cCAATxhrr_6aQAdPFU6tSCowhvS5JTK",
       "39J3nGR7GqUf8upt9WD0a1oBXd3_4GYhm6ZHkA3dbhewTvrH5",
       "39J43P5sSGaLaTnDlmPbBvTMKMp_5zipPsrY7AXusMUeBDJ5K"
   ]
   ```
4. Replace with your ngrok auth tokens
5. Save the file (Ctrl+S)
6. Restart the application

#### Step 7.2: Port Configuration
The application uses **Port 5000** for the Flask server. If this port is in use:

1. Open Command Prompt (Admin)
2. Check what's using port 5000:
   ```cmd
   netstat -ano | findstr :5000
   ```
3. If something is using it, either:
   - Stop the conflicting application
   - Use a different port by modifying the source code

---

### Phase 8: Verification Checklist

After setup, verify everything works:

- [ ] Python 3.7+ installed (`python --version` in CMD)
- [ ] All 5 packages installed (`pip show [package]` for each)
- [ ] Windows Firewall allows Python
- [ ] Application launches without errors
- [ ] "Boot Failover" connects to ngrok successfully
- [ ] Tunnel URL displays in status area
- [ ] You can open tunnel URL in browser
- [ ] Victim page shows "YOU GOT HONKED"
- [ ] Visiting the URL updates the map and terminal log
- [ ] Hit counter increments correctly

**If all items checked ✓ - Setup is complete and working!**

---

## Required Libraries & Installation (Reference)

### Detailed Package Information

| Library | Purpose | Installation | Minimum Version |
|---------|---------|--------------|-----------------|
| **pywebview** | Creates native desktop GUI windows | `pip install pywebview` | 5.0+ |
| **requests** | HTTP library for API calls | `pip install requests` | 2.28.0+ |
| **flask** | Lightweight web framework | `pip install flask` | 2.2.0+ |
| **pyngrok** | ngrok Python wrapper | `pip install pyngrok` | 7.0.0+ |
| **pyperclip** | Clipboard operations | `pip install pyperclip` | 1.8.2+ |

### Quick Commands Reference

**Install All Packages:**
```cmd
pip install pywebview requests flask pyngrok pyperclip
```

**Check Specific Package:**
```cmd
pip show pywebview
```

**Upgrade All Packages:**
```cmd
pip install --upgrade pywebview requests flask pyngrok pyperclip
```

**Create Requirements File:**
```cmd
pip freeze > requirements.txt
```

---

## Build Tool: Inno Setup

### Overview

**HONKED Security** is packaged and distributed using **Inno Setup**, a powerful, free script-driven installation system for Windows applications. Inno Setup creates professional Windows installers without requiring runtime files or DLLs.

### Inno Setup Configuration Details

#### Application Information
```
Application Name: HONKED_SECURITY BY CAPPIAVI
Version: 1.5
Publisher: Cappiavi, Khert Garde
Executable: myapp.exe
Unique Identifier (GUID): {1202F8A6-E6B9-46B3-8D39-CEE86C80445D}
```

#### Build Specifications

| Setting | Value | Purpose |
|---------|-------|---------|
| **Architecture** | 64-bit (x64) | 64-bit Windows systems only |
| **Architecture Target** | x64compatible | Compatibility with Windows 11 on ARM |
| **Install Mode** | 64-bit native | Uses Program Files directory |
| **Compression** | Solid Compression | Reduces installer file size |
| **Install Location** | `{autopf}\HONKED_SECURITY BY CAPPIAVI` | Program Files directory |
| **Output Filename** | mysetup.exe | Generated installer name |

#### Installation Features

1. **Desktop Icon Creation** (Optional)
   - Users can choose to create desktop shortcuts during installation
   - Located in `{autodesktop}` directory

2. **Registry Entries**
   - File association for application launch
   - Uninstall registry entries for Windows' Add/Remove Programs
   - Icon registry entries for Windows Explorer integration

3. **Program Group**
   - Automatic Start Menu shortcut creation
   - Located in `{autoprograms}` directory
   - Labeled as "HONKED_SECURITY BY CAPPIAVI"

#### File Handling

- **Source**: `C:\Users\User\Desktop\MyApp\dist\myapp.exe`
- **Destination**: `{app}` (Installation directory)
- **Flags**: Ignores existing file versions, ensures update functionality

#### Post-Installation Actions

- Automatic launch option available for first-time users
- "Launch Program" option in final dialog
- Checkbox to skip post-installation actions if needed

#### Visual Customization

- **Wizard Style**: Modern Dark Windows 11 style
- **Appearance**: Sleek dark interface matching contemporary Windows design
- Default language: English

### How Inno Setup Works

1. **Compilation Process**:
   - The `.iss` script files (`honkedsec.iss`, `honkinstaller.iss`) are compiled by Inno Setup
   - PyInstaller first converts Python code to `myapp.exe`
   - Inno Setup packages `myapp.exe` into a distributable installer

2. **Installation Process**:
   - User runs `mysetup.exe`
   - Inno Setup extracts and installs files to the specified directory
   - Creates registry entries and shortcuts
   - Launches application if post-install option selected

3. **Uninstallation**:
   - Inno Setup manages uninstall through Windows' "Add/Remove Programs"
   - Automatically cleans registry entries
   - Removes shortcuts and application files

### File Structure

```
FINAL/
├── HONKED SEC APP/
│   ├── honkedsec.iss              (Inno Setup script for HONKED Security)
│   ├── honkinstaller.iss          (Alternative installer configuration)
│   └── Output/
│       ├── HONKED SECURITY - CAPPIAVI v1.5.exe  (Compiled installer)
│       └── README.md               (This file)
```

---

## Project Structure

### Folder Organization

```
HONKED SECURITY APP PROJECTS/
├── Builds/
│   └── MyApp/                      (PyInstaller build output)
│       ├── honksec_installer.py   (Requirements installer script)
│       ├── myapp.py                (Main application wrapper)
│       ├── myapp.spec              (PyInstaller specification)
│       └── build/                  (Compiled binaries and artifacts)
│
├── FINAL/
│   └── HONKED SEC APP/
│       ├── honkedsec.iss           (Primary Inno Setup script)
│       ├── honkinstaller.iss       (Alternative installer script)
│       └── Output/
│           ├── HONKED SECURITY - CAPPIAVI v1.5.exe
│           └── README.md
│
└── Python End/
    └── Honked/
        ├── HONKED.py                (Base control panel application)
        ├── HONKED_ADVANCED.py       (Enhanced version)
        └── HONKSEC.py               (Modified security version)
```

### Core Application Files

- **HONKED.py**: Foundation application with basic functionality
- **HONKED_ADVANCED.py**: Feature-enhanced version with additional capabilities
- **HONKSEC.py**: Production version used in final builds with security optimizations
- **myapp.exe**: PyInstaller-compiled executable (Windows-only)

---

## How to Use HONKED Security After Setup

### Basic Operation Workflow

#### 1. Starting the Application
**Most Common Method (Installed Version):**
1. Double-click desktop shortcut **"HONKED_SECURITY BY CAPPIAVI"**
2. Wait 3-5 seconds for the control panel to appear
3. You should see a dark green-themed window with left sidebar and map area

**Alternative Methods:**
- Find in Start Menu: Press Windows Key, type "HONKED", press Enter
- Command line: Run `python HONKSEC.py` from the Python End/Honked directory

#### 2. Initialize the Tunnel System
1. When the application starts, the status indicator will be RED (offline)
2. Click the **"Boot Failover"** button on the left sidebar
3. Wait 5-10 seconds while ngrok connects
4. You'll see terminal messages: "[SYSTEM] Uplink 01 Online"
5. Status indicator turns GREEN
6. A public URL appears (example: `https://1a2b3c4d.ngrok.io`)

#### 3. Using the Generated URL
**To Share the Tunnel:**
1. Click **"Copy Link"** button
2. URL is now in your clipboard
3. Share it via email, messaging, or any platform
4. When someone visits the URL, they'll see the "YOU GOT HONKED" page

**To Test Locally:**
1. Copy the URL (click "Copy Link")
2. Open any web browser
3. Paste the URL and press Enter
4. You should see the animated "YOU GOT HONKED" page
5. In your control panel, the terminal logs the hit with your IP and location

#### 4. Monitoring Visitors
1. Every time someone visits your tunnel URL:
   - **Terminal Log** (bottom right) shows: `[!] HIT DETECTED: [IP] | [City Name]`
   - **Interactive Map** (top right) updates with red marker at visitor's location
   - **Hit Counter** increases (if available)
   - **Visual Alert**: Blinking "YOU GOT HONKED" page displays to visitor
   - **Audio Alert**: Plays only in development mode (source code version with music.mp3)

#### 5. Manual IP Lookup
To manually trace any IP address:
1. Click **"Trace IP"** button
2. Enter an IP address in the prompt
3. The application displays geolocation data for that IP
4. Map updates to show that location

#### 6. Toggling Victim Mode
1. Click **"Toggle Status"** button to switch between:
   - **ACTIVE**: Visitors see the "YOU GOT HONKED" page normally
   - **OFFLINE**: Visitors see "404 - SESSION EXPIRED" instead
2. Use this to pause the application without disconnecting

#### 7. Shutdown Procedure
1. When finished, click the red **"Shutdown"** button
2. Application closes
3. ngrok tunnel terminates
4. All URLs become inactive

---

## System Requirements

| Requirement | Specification |
|------------|---------------|
| **OS** | Windows 10 or Windows 11 (64-bit) |
| **Architecture** | x64 processor |
| **Python** | 3.7 or higher (for source version) |
| **RAM** | Minimum 512MB; Recommended 2GB+ |
| **Disk Space** | ~200MB for installation |
| **Network** | Active internet connection required |
| **Ports** | 5000 (Flask server, tunneled via ngrok) |

---

## Technical Details

### Backend Stack

- **Framework**: Flask 2.x
- **Web Server**: WSGI (Werkzeug)
- **Geolocation**: ip-api.com (free tier)
- **Tunneling**: ngrok (requires authentication keys)
- **Desktop GUI**: pywebview

### Frontend Stack

- **HTML5/CSS3**: Control panel UI
- **JavaScript**: Real-time DOM manipulation and AJAX calls
- **Leaflet.js**: Interactive mapping library
- **Canvas API**: Matrix-style animations

### Key APIs & Services

1. **ngrok**: Creates secure tunnels and public URLs
   - Multiple cluster keys for failover
   - Token authentication via `CLUSTER_KEYS` array
   - Automatic reconnection on failure

2. **IP-API**: Geolocation and IP information
   - Returns comprehensive location data (city, country, coordinates)
   - Rate-limited free tier: 45 requests/minute

3. **pywebview**: Native window management
   - Runs HTML/CSS/JS in platform-native WebKit
   - Bidirectional communication between Python and JavaScript

---

## Build & Compilation Information

### PyInstaller Configuration

The application is compiled to Windows executables using **PyInstaller**:

- **Spec File**: `myapp.spec`
- **Mode**: Binary (single executable)
- **Compression**: Enabled
- **Output**: `myapp.exe` in dist/ folder

### Inno Setup Compilation

Installer creation follows two potential paths:

1. **Primary Path** (`honkedsec.iss`):
   - Creates branded installer with custom styling
   - Integration with Windows 11 dark theme
   - Professional installation wizard

2. **Alternative Path** (`honkinstaller.iss`):
   - Backup configuration
   - Alternative installer branding options

### Version Control

- **Current Version**: 1.5
- **Last Updated**: [Specified in installer metadata]
- **Build Date**: [Embedded in compiled executable]

---

## IMPORTANT: Audio Limitations & Technical Explanation

### Audio Support Summary

**CRITICAL INFORMATION:**
- ❌ Audio **NOT SUPPORTED** in installed compiled version (`.exe`)
- ✅ Audio **ONLY WORKS** when running source code from terminal (`python HONKSEC.py`)
- ✅ All other features (visuals, tracking, mapping) work perfectly without audio

---

### Why Audio Doesn't Work in Compiled Software

#### Technical Explanation

When HONKED Security is compiled from Python source code to a Windows executable (`.exe`), a fundamental limitation exists with how audio files are handled:

**1. PyInstaller Compilation Process**

PyInstaller converts Python code to a standalone `.exe` executable by:
- Analyzing all imports and dependencies
- Bundling Python runtime
- Compiling to machine code
- Creating a single self-contained binary

However, **PyInstaller does NOT embed arbitrary data files** (like audio) in the final executable unless specifically configured in the `.spec` file.

**2. Root Cause: File Path Resolution**

In the source Python code (`HONKSEC.py`), the Flask server serves audio with:
```python
@flask_app.route('/music.mp3')
def serve_music():
    return send_from_directory(os.getcwd(), 'music.mp3')
```

This code looks for `music.mp3` in the **current working directory** (`os.getcwd()`).

**Problem:**
- When running from terminal: `os.getcwd()` = folder containing `HONKSEC.py`
- When installed as `.exe`: `os.getcwd()` = `C:\Program Files\HONKED_SECURITY BY CAPPIAVI\` OR user's current directory
- The installer (`Inno Setup`) doesn't include `music.mp3` in the Package
- **Result:** File path resolution fails, audio cannot be served

**3. Pyinstaller Hidden Data Limitation**

To include `music.mp3` in a compiled `.exe`, it would require:

a) **In the `.spec` file:**
```python
datas=[('path/to/music.mp3', '.')]
```
b) **Recompilation** of the entire application
c) **Complex path handling** in source code to access bundled resources

Since the current build does not include this configuration, the audio file is inaccessible.

**4. Browser Security Context**

Additionally, when Flask serves from a bundled source:
- File paths become ambiguous in the compiled binary
- Security sandboxing may prevent file access
- HTML5 `<audio>` element cannot reliably access resources

---

### Development Mode vs. Production Mode

| Feature | Development Mode (`python HONKSEC.py`) | Installed `.exe` Version |
|---------|----------------------------------------|--------------------------|
| **Audio Support** | ✅ YES (music.mp3 required) | ❌ NO |
| **Visual "YOU GOT HONKED"** | ✅ YES | ✅ YES |
| **Matrix Animation** | ✅ YES | ✅ YES |
| **IP Tracking** | ✅ YES | ✅ YES |
| **Geolocation Map** | ✅ YES | ✅ YES |
| **Hit Detection** | ✅ YES | ✅ YES |
| **Terminal Logging** | ✅ YES | ✅ YES |
| **ngrok tunneling** | ✅ YES | ✅ YES |
| **File Dependencies** | Requires source folder | Standalone executable |

---

### Using HONKED Security Without Audio

**The installed version works perfectly without audio:**

1. **Visual Alerts Are Sufficient:**
   - Bright red "YOU GOT HONKED" text
   - Blinking animation draws attention
   - Matrix-style background adds drama

2. **Terminal Notifications:**
   - Control panel terminal logs all hits: `[!] HIT DETECTED: [IP] | [City]`
   - Color-coded messages (green text) stand out
   - Hit counter increments visible in UI

3. **Alternative Alerts:**
   - Windows notification popup (Windows handles this)
   - System tray icon state change
   - Control panel window highlight on taskbar

4. **Production Recommendation:**
   - Use installed `.exe` version (recommended, reliable, standalone)
   - Audio is optional - the visual feedback is sufficient
   - No external dependencies or setup required

---

### If You Need Audio

To use HONKED Security WITH audio, you must run it from source code:

1. **Install Python and dependencies** (see Phase 2 & Phase 3 of setup guide)
2. **Ensure `music.mp3` exists** in:
   ```
   C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\Python End\Honked\music.mp3
   ```
3. **Run from terminal:**
   ```cmd
   cd C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\Python End\Honked\
   python HONKSEC.py
   ```
4. **Audio will play** when visitors access the tunnel URL

**Drawbacks of Source Mode:**
- Requires Python installed on target machine
- Slower startup than compiled `.exe`
- Dependent on file system organization
- Not portable like `.exe`
- Requires Python knowledge to modify

---

### Conclusion

**Best Practice:** Use the installed `.exe` version (delivered without audio) for:
- ✅ Simplicity (no dependencies)
- ✅ Portability (works anywhere)
- ✅ Performance (faster execution)
- ✅ Reliability (no path dependencies)

The application is **fully functional and recommended for use WITHOUT audio**.

---

## Complete System Requirements & Verification

### Detailed System Requirements

#### Operating System
- **Windows 10**: Build 1909 or later (released November 2019)
- **Windows 11**: All versions (2021 or later)
- **Architecture**: 64-bit (x64) only - 32-bit systems NOT supported
- **Processor**: Intel Core 2, AMD Athlon 64, or newer
- **RAM**: Minimum 2GB (4GB+ recommended for smooth operation)
- **Disk Space**: 
  - 300MB for installation
  - 500MB for cache and temporary files
  - Total: 1GB free space recommended

#### Network Requirements
- **Internet Connection**: Broadband (minimum 1 Mbps upload/download)
- **Ports**: 5000 (Flask server) - automatically tunneled through ngrok
- **Firewall Rules**: Must allow outbound connections to ngrok.com and api.ip-api.com
- **DNS**: Must be able to resolve DNS names

#### Software Requirements
- **Python**: 3.7, 3.8, 3.9, 3.10, 3.11, or 3.12
- **pip**: Included with Python 3.4+
- **Windows Updates**: Current (latest Windows Update installed)
- **Visual C++ Redistributable**: Installed automatically with Python

### Pre-Installation System Verification Checklist

Use this checklist to verify your system is ready before installing:

**Windows Version:**
```
[ ] Windows 10 (Build 1909+) OR Windows 11
[ ] System is 64-bit (Settings > System > About > "System type: 64-bit")
```

**Hardware:**
```
[ ] RAM: At least 2GB (verify in Settings > System > About)
[ ] Free Disk Space: At least 1GB (Right-click drive > Properties)
[ ] Processor: Supports virtualization (BIOS enabled)
```

**Network:**
```
[ ] Internet connection active and stable
[ ] Can access https://www.google.com in browser
[ ] Can access https://ngrok.com in browser
[ ] Can access https://api.ip-api.com in browser
```

**Software:**
```
[ ] Python 3.7+ installed (python --version in CMD)
[ ] pip working correctly (pip --version in CMD)
[ ] Windows Firewall enabled or third-party firewall configured
```

**Permissions:**
```
[ ] User account has administrator rights
[ ] Can run programs "as administrator"
[ ] Can create files in Program Files directory
```

### Post-Installation Verification

After installation, verify everything works correctly:

#### Step 1: Verify Python Installation
```cmd
python --version
python -c "import sys; print(f'Python executable: {sys.executable}')"
```
Expected output: Python version number and executable path

#### Step 2: Verify All Packages Installed
```cmd
pip list | findstr /E "pywebview requests flask pyngrok pyperclip"
```
Expected output: All 5 packages with version numbers

#### Step 3: Test Package Imports
```cmd
python -c "import pywebview; import requests; import flask; import pyngrok; import pyperclip; print('All packages imported successfully')"
```
Expected output: "All packages imported successfully"

#### Step 4: Verify Installer Location
Navigate to: `C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\FINAL\HONKED SEC APP\Output\`

Verify files exist:
- `HONKED SECURITY - CAPPIAVI v1.5.exe` ✓
- `README.md` ✓

#### Step 5: Verify Installation
Check Control Panel > Programs and Features
- Should see "HONKED_SECURITY BY CAPPIAVI"
- Version should show "1.5"

Check Start Menu:
- Press Windows Key
- Type "HONKED"
- Should see "HONKED_SECURITY BY CAPPIAVI" in results

#### Step 6: Test Application Launch
1. Double-click desktop shortcut OR
2. Use Start Menu > HONKED_SECURITY BY CAPPIAVI

Expected behavior:
- Application window opens within 5-10 seconds
- Black window with green text appears
- No error messages

#### Step 7: Test ngrok Connection
1. Application is running and visible
2. Click "Boot Failover" button
3. Wait 10 seconds
4. Check for:
   - Terminal message: "[SYSTEM] Uplink 01 Online"
   - Status indicator turns GREEN
   - URL appears in status area (format: `https://[something].ngrok.io`)

#### Step 8: Test Victim Page
1. Copy the ngrok URL (click "Copy Link")
2. Open web browser
3. Paste URL and press Enter
4. Expected page:
   - Black background
   - Green text: "YOU GOT HONKED"
   - Matrix-style animation running
   - **Note**: Audio unavailable in compiled `.exe` (development mode only)

#### Step 9: Test Hit Detection
1. Open the tunnel URL in browser (or have someone else visit it)
2. Check application terminal (bottom right)
3. Should see: "[!] HIT DETECTED: [Your IP] | [Your City]"
4. Check map (top right):
   - Should show red marker at your location
5. Check hit counter:
   - Should increment by 1 (if feature available)

#### Step 10: Test Shutdown
1. Click red "Shutdown" button
2. Application should close cleanly
3. No error messages
4. ngrok tunnel should be terminated

**If all 10 steps pass ✓ - Application is fully functional!**

---

## Quick Reference Guide

### Essential Commands

**Check Python Version:**
```cmd
python --version
```

**Check pip Version:**
```cmd
pip --version
```

**Install All Dependencies:**
```cmd
pip install pywebview requests flask pyngrok pyperclip
```

**Check Specific Package:**
```cmd
pip show pywebview
```

**Check If Port 5000 is In Use:**
```cmd
netstat -ano | findstr :5000
```

**Start Application (Source Version):**
```cmd
cd C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\Python End\Honked\
python HONKSEC.py
```

**Get Your Public IP:**
```cmd
python -c "import requests; print(requests.get('https://api.ip-api.com/json/').json()['query'])"
```

### Common File Locations

**Install Location:**
```
C:\Program Files\HONKED_SECURITY BY CAPPIAVI\
```

**Source Code Location:**
```
C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\Python End\Honked\
```

**Installer Location:**
```
C:\Users\[YourUsername]\Desktop\HONKED SECURITY APP PROJECTS\FINAL\HONKED SEC APP\Output\
```

**Python Location (Example for 3.11):**
```
C:\Users\[YourUsername]\AppData\Local\Programs\Python311\
```

### Keyboard Shortcuts in Application

| Action | Shortcut |
|--------|----------|
| Copy tunnel URL | Click "Copy Link" button |
| Toggle terminal | Scroll in terminal area |
| Refresh map | F5 in browser window |
| Full screen | F11 in browser window |
| Developer tools | F12 in victim page (browser) |
| Exit application | Click "Shutdown" button |

### Network Ports

| Service | Port | Protocol | Direction |
|---------|------|----------|-----------|
| Flask Server | 5000 | HTTP | Local only |
| ngrok Tunnel | 443 | HTTPS | Outbound |
| IP-API | 443 | HTTPS | Outbound |
| DNS | 53 | UDP | Outbound |

### Useful Websites

| Service | URL | Purpose |
|---------|-----|---------|
| ngrok | https://ngrok.com | Tunnel management & keys |
| IP-API | https://api.ip-api.com | Geolocation testing |
| Python | https://www.python.org | Download & documentation |
| What's my IP | https://whatismyip.com | Verify public IP |
| Speed Test | https://speedtest.net | Test internet speed |

---

## Advanced Configuration Guide

### 1. Changing Installation Directory

If you want to install to a different location:

1. **Before running installer:**
   - Don't run installer yet
   - You'll get choice during installation

2. **During installation:**
   - At "Select Installation Folder" screen
   - Click "Browse"
   - Choose desired location (must be empty folder)
   - Must have read/write permissions
   - Continue with installation

3. **Update shortcuts:**
   - Start Menu shortcuts auto-update
   - Desktop shortcut needs manual update if moved

### 2. Running Multiple Instances

**Warning:** Not recommended - will cause port conflicts

If you must run multiple instances:
1. Edit source code in HONKSEC.py
2. Change port 5000 to 5001, 5002, etc. (lines with Flask)
3. Ensure each instance uses different port
4. Run each with separate Python instance

### 3. Custom Cluster Keys Setup

To use your own ngrok account:

1. **Create ngrok account:**
   - Visit https://ngrok.com
   - Sign up (free tier available)
   - Login to dashboard
   - Copy your auth token

2. **Update application:**
   - Open: `HONKSEC.py` in text editor
   - Find CLUSTER_KEYS section (around line 10)
   - Replace all 3 keys with your auth token (duplicate 3x for failover):
   ```python
   CLUSTER_KEYS = [
       "your_auth_token_here",
       "your_auth_token_here",
       "your_auth_token_here"
   ]
   ```
   - Save file
   - Restart application

### 4. Modifying Victim Page Content

To customize the "YOU GOT HONKED" message:

1. **Locate source code:**
   - Open: `HONKSEC.py` in text editor
   - Search for "YOU GOT HONKED" (around line 65)

2. **Edit text:**
   - Change "YOU GOT HONKED" to desired text
   - Change "I KNOW WHERE U AT BRO" to custom message
   - Change "CAPPIAVI" credit to your name

3. **Save and restart:**
   - Save file
   - Restart application
   - Test victim page to confirm changes

### 5. Firewall Whitelist (Advanced)

For Windows Firewall Advanced Settings:

1. Open Windows Defender Firewall
2. "Inbound Rules" > "New Rule"
3. Select "Program"
4. Browse to: `C:\Program Files\HONKED_SECURITY BY CAPPIAVI\myapp.exe`
5. Select "Allow the connection"
6. Check all: Domain, Private, Public
7. Name: "HONKED Security"
8. Finish

Repeat for:
- Outbound Rules
- port.exe (if running from source)

---

## Uninstall Instructions

### Uninstall HONKED Security

**Method 1 (Recommended):**
1. Click Start button (Windows key)
2. Type: "Add or remove programs"
3. Find "HONKED_SECURITY BY CAPPIAVI"
4. Click it
5. Click "Uninstall"
6. Click "Remove"
7. Follow wizard to completion
8. Click "Finish"

**Method 2 (Control Panel):**
1. Right-click Start button
2. Select "Settings"
3. Click "Apps" > "Apps & features"  
4. Search: "HONKED"
5. Click result
6. Click "Uninstall"
7. Follow wizard

**Method 3 (Manual):**
1. Delete folder: `C:\Program Files\HONKED_SECURITY BY CAPPIAVI\`
2. Delete Start Menu shortcut:
   - `C:\Users\[YourUsername]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\HONKED_SECURITY BY CAPPIAVI.lnk`
3. Delete Desktop shortcut (if exists)
4. Open Registry Editor:
   - Press Windows+R
   - Type: `regedit`
   - Navigate to: `HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\`
   - Find and delete: `{1202F8A6-E6B9-46B3-8D39-CEE86C80445D}`

### Uninstall Python Packages

```cmd
pip uninstall pywebview requests flask pyngrok pyperclip -y
```

### Uninstall Python (Optional)

1. Control Panel > Programs and Features
2. Find "Python 3.x"
3. Click "Uninstall"
4. Select "Uninstall"
5. Wait for completion
6. Restart computer

*Note: Uninstalling Python is optional. Keep it if you plan to use Python for other projects.*

**Developer**: Cappiavi & Khert Garde  
**Application**: HONKED Security Control Panel  
**Version**: 1.5  
**License**: Proprietary (Non-commercial use noted in Inno Setup configuration)

---

## Important Notes

⚠️ **Legal Disclaimer**: This application should only be used for authorized security testing and monitoring. Unauthorized access to computer systems is illegal. Ensure you have proper authorization before deploying this application.

⚠️ **ngrok Configuration**: The CLUSTER_KEYS array contains authentication tokens required to use ngrok. These are specific to the account and should be kept secure.

⚠️ **Data Privacy**: The application logs IP addresses and geolocation data. Ensure compliance with privacy regulations where deployed.

---

## Comprehensive Troubleshooting Guide

### Installation Issues

#### Problem: "python is not recognized as an internal or external command"

**Cause:** Python is not installed OR not added to PATH

**Solution:**
1. Verify Python installation:
   - Check if Python is installed: Go to `C:\Users\[YourName]\AppData\Local\Programs\Python\`
   - Look for folders like `Python311`, `Python310`, etc.
   
2. If folder exists, add Python to PATH:
   - Press Windows Key
   - Search: "Edit environment variables"
   - Click "Edit the system environment variables"
   - Click "Environment Variables" button (bottom right)
   - Under "System variables", click "Edit" on "Path"
   - Click "New"
   - Add: `C:\Users\[YourName]\AppData\Local\Programs\Python311` (adjust version number)
   - Add another entry: `C:\Users\[YourName]\AppData\Local\Programs\Python311\Scripts`
   - Click OK three times
   - Restart Command Prompt and try `python --version` again

3. If folder doesn't exist, reinstall Python:
   - Download from https://www.python.org/downloads/
   - Run installer
   - **IMPORTANT**: Check "Add Python to PATH" before installing
   - Click "Install Now"

#### Problem: "No module named 'pip'" or pip commands fail

**Cause:** pip is not installed or Python is misconfigured

**Solution:**
```cmd
python -m ensurepip --default-pip
```

Then retry installation:
```cmd
pip install pywebview requests flask pyngrok pyperclip
```

#### Problem: "pip install" downloads but fails to install

**Cause:** Missing Visual C++ compiler or permission issues

**Solution:**
1. Download Visual Studio Build Tools:
   - Visit: https://visualstudio.microsoft.com/visual-cpp-build-tools/
   - Run the installer
   - Select "Desktop development with C++"
   - Install

2. Run Command Prompt as Administrator again:
   - Press Windows Key + R
   - Type: `cmd`
   - Press Ctrl+Shift+Enter (not just Enter)
   - Try pip install again

#### Problem: "Permission denied" or "Access is denied"

**Cause:** Not running with administrator privileges

**Solution:**
1. Press Windows Key
2. Type: `cmd`
3. Right-click "Command Prompt"
4. Select "Run as administrator"
5. Click "Yes"
6. Run pip install command

---

### Package Installation Issues

#### Problem: "ERROR: Could not find a version that satisfies the requirement"

**Cause:** Typo in package name OR using Python version that's too old

**Solution:**
```cmd
pip install --upgrade pip
pip install pywebview requests flask pyngrok pyperclip
```

If that fails, install each package individually:
```cmd
pip install pywebview
pip install requests
pip install flask
pip install pyngrok
pip install pyperclip
```

#### Problem: Package installs but still says "No module named..."

**Cause:** Multiple Python installations (e.g., Python from different sources)

**Solution:**
1. Identify which Python is running:
   ```cmd
   python -c "import sys; print(sys.executable)"
   ```
   Take note of the path.

2. Use that specific Python for pip:
   ```cmd
   C:\path\from\above\python -m pip install pywebview requests flask pyngrok pyperclip
   ```

---

### Installer Issues

#### Problem: Installer crashes or says "Cannot find myapp.exe"

**Cause:** Build files missing or installer is corrupted

**Solution:**
1. Delete the existing installer: `HONKED SECURITY - CAPPIAVI v1.5.exe`
2. Reinstall from the build folder using Inno Setup
3. Or download a fresh copy of the installer

#### Problem: "Access Denied" when running installer

**Cause:** Another version is running OR Windows security settings

**Solution:**
1. Close all Python windows/applications
2. Right-click installer
3. Select "Run as administrator"
4. Click "Yes" at UAC prompt

#### Problem: "Disk space insufficient" error

**Cause:** Less than 500MB free disk space

**Solution:**
1. Free up disk space:
   - Open File Explorer
   - Right-click C: drive
   - Select "Clean up System Files"
   - Delete temporary files
   
2. Ensure 1GB+ free space before reinstalling

---

### Runtime Issues

#### Problem: Application starts but window doesn't appear

**Cause:** pywebview not rendering OR display scaling issues

**Solution:**
1. Wait 10 seconds (window can take time to load)
2. Check if window is minimized (look in taskbar)
3. Reinstall pywebview:
   ```cmd
   pip uninstall pywebview
   pip install --upgrade pywebview
   ```

#### Problem: "ngrok connection failed" or "All keys exhausted"

**Cause:** Invalid cluster keys OR ngrok service down OR internet issues

**Solution:**
1. Check internet connection:
   - Open browser
   - Visit https://ngrok.com
   - If it loads, internet is fine
   
2. Verify cluster keys are valid:
   - Go to https://ngrok.com
   - Login to your account
   - Copy your valid auth token
   - Edit the source file:
     - Open: `C:\Users\[YourName]\Desktop\HONKED SECURITY APP PROJECTS\Python End\Honked\HONKSEC.py`
     - Find the CLUSTER_KEYS section (around line 10)
     - Replace with your valid token

3. Try clicking "Boot Failover" again

#### Problem: Application launches but "Boot Failover" button doesn't work

**Cause:** ngrok keys are invalid OR port 5000 already in use

**Solution:**
1. Check if port 5000 is busy:
   ```cmd
   netstat -ano | findstr :5000
   ```
   - If it shows a process ID (PID), something is using the port
   - Either close that application OR modify the source code to use a different port

2. Verify ngrok keys (see solution above)

3. Check Windows Firewall:
   - Make sure Python is allowed through firewall
   - See Phase 4, Step 4.3 in setup guide

#### Problem: Tunnel URL opens but shows "502 Bad Gateway"

**Cause:** Flask server not running properly OR long response time

**Solution:**
1. Wait 10-15 seconds
2. Refresh the browser (press F5)
3. If still fails, restart the application:
   - Click red "Shutdown" button
   - Wait 5 seconds
   - Launch application again
   - Click "Boot Failover"

#### Problem: Visitor hits don't appear on map or terminal

**Cause:** Map library not loading OR terminal has scrolled

**Solution:**
1. Open browser Developer Tools:
   - Press F12 in browser
   - Check "Console" tab for JavaScript errors
   
2. Check if JavaScript is enabled:
   - In browser, look at address bar
   - If you see a warning icon, click and enable JavaScript
   
3. Try refreshing page (F5)

---

### Performance Issues

#### Problem: Application is very slow or freezes

**Cause:** Low system resources OR ngrok is lagging

**Solution:**
1. Close other applications:
   - Close web browsers
   - Close video/music players
   - Close heavy applications

2. Increase virtual memory:
   - Right-click "This PC"
   - Select "Properties"
   - Left sidebar: "Advanced system settings"
   - "Performance" section > "Settings"
   - "Advanced" tab > "Change" (Virtual memory)
   - Set custom size: 4096-8192 MB
   - Click "Set" then "OK"

3. Restart computer and try again

#### Problem: ngrok times out or disconnects frequently

**Cause:** Internet connection instability OR firewall issues

**Solution:**
1. Check internet speed:
   - Visit https://speedtest.net
   - Upload/Download should be at least 1 Mbps each
   - If much slower, contact ISP

2. Configure firewall to allow ngrok:
   - Windows Defender Firewall > Allow app through
   - Find "Python" entries
   - Check both Private and Public

3. Reduce application load:
   - Don't open multiple tunnel URLs simultaneously
   - Close other internet-heavy applications

---

### Audio/Visual Issues

#### Problem: Audio doesn't play on victim page

**Cause:** **IMPORTANT - Audio is intentionally DISABLED in the compiled installer version**

Because of how PyInstaller compiles Python to `.exe`, audio files embedded in the source code are not accessible at runtime in the compiled binary. See the "AUDIO LIMITATIONS" section below for detailed technical explanation.

**Solution:**
1. **First, understand:** Audio ONLY works when running from source code terminal, NOT from the installed `.exe`

2. **If running from installed software (.exe):**
   - Audio is NOT supported - this is a limitation of PyInstaller compilation
   - The visual "YOU GOT HONKED" page still displays correctly
   - Animation and all other features work normally
   - This is expected behavior and not an error

3. **If running from source code (development mode):**
   - Audio will work if `music.mp3` exists in the source folder
   - Run: `python HONKSEC.py` from terminal
   - Visitor page will include audio

4. **For production use (recommended):**
   - Use the installed `.exe` version without audio
   - The application works perfectly without sound
   - Focus on visual alerts and terminal notifications instead

#### Problem: Matrix animation doesn't display on victim page

**Cause:** JavaScript disabled OR outdated browser

**Solution:**
1. Check browser:
   - Use modern browser: Chrome, Firefox, Edge (not Internet Explorer)
   - Download latest version from microsoft.com (for Edge)

2. Enable JavaScript:
   - In browser address bar, if you see a warning icon, click it
   - Enable JavaScript

3. Clear browser cache:
   - Press Ctrl+Shift+Delete
   - Select "All time"
   - Check all boxes
   - Click "Delete"
   - Refresh page

---

### Data Issues

#### Problem: Hit count shows 0 or doesn't increment

**Cause:** Visitor page not being served correctly OR JavaScript not running

**Solution:**
1. Test the URL directly:
   - Copy tunnel URL
   - Open in new browser window (not tab)
   - Verify you see "YOU GOT HONKED" page
   
2. Check if hit appears in terminal:
   - Look at bottom right "Terminal" section
   - Should show: "[!] HIT DETECTED: [IP] | [City]"
   - If appears in terminal but not in counter, refresh the map area

#### Problem: Map shows wrong location for visitor

**Cause:** IP-API returning incorrect data OR IP is from VPN/Proxy

**Solution:**
1. The application uses ip-api.com for geolocation (free tier)
2. If visitor uses VPN, location will be VPN server location, not actual location
3. This is expected behavior and not an error

#### Problem: Geolocation data shows "Unknown" or "No Data"

**Cause:** IP-API rate limit exceeded OR invalid IP format

**Solution:**
1. Wait 5-10 minutes (IP-API free tier: 45 requests/minute)
2. If tracing IP manually:
   - Ensure format is correct (e.g., 8.8.8.8, not "8.8.8.8/24")
   - Try a known IP like 1.1.1.1 to verify service works

---

### Network/Firewall Issues

#### Problem: Antivirus/Windows Defender blocks the application

**Cause:** Application behavior triggers security alerts

**Solution:**
1. Add to Windows Defender exclusions:
   - Press Windows Key
   - Type: "Virus & threat protection"
   - Click "Manage settings"
   - Scroll to "Exclusions"
   - Click "Add exclusions"
   - Add: `C:\Program Files\HONKED_SECURITY BY CAPPIAVI\`

2. Disable real-time scanning (not recommended for production):
   - In Windows Security
   - Virus & threat protection
   - Disable "Real-time protection" toggle

3. Use different antivirus:
   - Some third-party antivirus is overly aggressive
   - Consider switching to Windows Defender only

#### Problem: "Connection refused" when opening tunnel URL

**Cause:** Flask server didn't start OR port blocked

**Solution:**
1. Ensure "Boot Failover" completed successfully:
   - Terminal should show "[SYSTEM] Uplink 01 Online"
   - Status indicator should be GREEN
   
2. Check Flask is running:
   - Click red "Shutdown" button
   - Wait 5 seconds
   - Launch application again
   - Click "Boot Failover"
   - Immediately open tunnel URL in new browser

3. Check firewall:
   - Go to Windows Defender Firewall
   - Allow Python through firewall
   - Restart application

#### Problem: Can access tunnel URL but visitors can't

**Cause:** Firewall settings OR network configuration

**Solution:**
1. Give network access to Python:
   - Windows Defender Firewall
   - "Allow an app through firewall"
   - Find Python
   - Check both "Private" AND "Public"
   - Click OK

2. Test from another device on same network:
   - Use phone or tablet on same WiFi
   - Open the tunnel URL
   - If works, issue is external network
   - If fails, issue is local firewall

---

### Reinstall/Reset

#### Complete Clean Reinstall

If nothing else works, do a complete clean reinstall:

1. **Uninstall Python packages**:
   ```cmd
   pip uninstall pywebview requests flask pyngrok pyperclip -y
   ```

2. **Uninstall the application**:
   - Go to Control Panel > Programs > Programs and Features
   - Find "HONKED_SECURITY BY CAPPIAVI"
   - Click it
   - Select "Uninstall"
   - Click "Remove"
   - Wait for completion

3. **Remove Python** (optional):
   - Control Panel > Programs and Features
   - Find "Python 3.x"
   - Click "Uninstall"
   - Restart computer

4. **Fresh install**:
   - Follow the complete setup guide from Phase 1 again

---

### Getting Help

If you've tried all troubleshooting steps and still have issues:

1. **Collect system information**:
   - Windows version (Settings > System > About)
   - Python version (`python --version`)
   - List of installed packages (`pip list`)

2. **Check error messages**:
   - If application shows error, note exact message
   - Include error in support request

3. **Log files**:
   - If application creates logs, include them
   - Usually in application folder or Documents

4. **Contact developer**:
   - Developer: Cappiavi & Khert Garde
   - Include all information from steps 1-3

---

**End of README - HONKED SECURITY v1.5**