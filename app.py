from flask import Flask, request
import os
app = Flask(__name__)

visitas = 0
ips = []

@app.route("/")
def home():
    global visitas, ips
    visitas += 1
    ip = request.remote_addr
    ips.append(ip)
    return f"""
    <!doctype html>
<html lang="es">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>!!! SYSTEM BREACH !!!</title>
  <style>
    *{{box-sizing:border-box;margin:0;padding:0}}
    html,body{{height:100%}}
    body{{
      background:#0a0a0a;
      color:#00ff41;
      font-family:'Courier New', 'Consolas', monospace;
      overflow:hidden;
    }}

    .matrix{{position:fixed;inset:0;z-index:0;}}
    canvas{{width:100%;height:100%;display:block}}

    .panel{{position:relative;z-index:2;padding:40px;max-width:1200px;
      margin:30px auto;background:rgba(0,0,0,0.85);
      border:2px solid rgba(0,255,65,0.15);
      box-shadow:0 0 50px rgba(0,255,65,0.1), inset 0 0 30px rgba(0,0,0,0.8);
      border-radius:8px;backdrop-filter:blur(8px)}}

    h1{{font-size:42px;letter-spacing:3px;color:#ff0040;
      text-shadow:0 0 20px rgba(255,0,64,0.4), 0 0 40px rgba(255,0,64,0.2);
      text-align:center;margin-bottom:20px;
      font-weight:bold;text-transform:uppercase}}

    .status{{color:#00ff41;font-size:16px;margin-bottom:25px;
      text-align:center;opacity:0.8}}

    .log{{margin-top:25px;background:rgba(0,0,0,0.9);padding:20px;
      border-radius:4px;height:350px;overflow:auto;
      border:1px solid rgba(0,255,65,0.2);
      box-shadow:inset 0 0 20px rgba(0,0,0,0.8)}}
    .log > div{{font-size:15px;line-height:1.6;color:#00ff41;
      padding:2px 0;border-left:3px solid rgba(0,255,65,0.3);
      padding-left:10px;margin:3px 0}}

    .modal{{position:fixed;inset:0;display:flex;align-items:center;
      justify-content:center;padding:24px;z-index:9;visibility:hidden;
      opacity:0;transition:all .3s;background:rgba(0,0,0,0.8)}}
    .modal.show{{visibility:visible;opacity:1}}
    .modal .card{{background:#0a0a0a;padding:30px;border-radius:8px;
      max-width:800px;border:2px solid rgba(0,255,65,0.3);
      box-shadow:0 0 40px rgba(0,255,65,0.2)}}
    .modal h2{{color:#00ff41;font-size:28px;text-align:center;margin-bottom:15px}}
    .modal p{{color:#ccffcc;margin-top:12px;font-size:16px;line-height:1.5}}

    footer{{position:fixed;left:15px;bottom:15px;z-index:3;
      font-size:12px;color:rgba(0,255,65,0.4);
      text-shadow:0 0 5px rgba(0,255,65,0.2)}}
  </style>
</head>
<body>
  <div class="matrix"><canvas id="matrixCanvas"></canvas></div>

  <div class="panel" role="main">
    <h1>!!! SYSTEM BREACH !!!</h1>
    <p class="status">Conexiones activas: {visitas}</p>
    <div class="log" id="log" aria-live="polite"></div>
  </div>

  <div class="modal" id="modal">
    <div class="card">
      <h2>¡¡BROMAAA 😅!!</h2>
      <p>No abras enlaces desconocidos. Esta simulación fue para demostrar lo fácil que es hacer parecer un hackeo.</p>
      <p>👉 Confía en mis enlaces, pero desconfía de otros 😉</p>
    </div>
  </div>

  <footer>Prank demo • Uso educativo</footer>

  <script>
    // MATRIX BACKGROUND
    const canvas = document.getElementById('matrixCanvas');
    const ctx = canvas.getContext('2d');
    let cols, rows, size = 14, drops;
    function resize(){{
      canvas.width = innerWidth; canvas.height = innerHeight;
      cols = Math.floor(canvas.width / size);
      rows = Math.floor(canvas.height / size);
      drops = new Array(cols).fill(1);
    }}
    window.addEventListener('resize', resize);
    resize();
    function frame(){{
      ctx.fillStyle = 'rgba(0,0,0,0.06)';
      ctx.fillRect(0,0,canvas.width,canvas.height);
      ctx.fillStyle = '#00ff6a'; ctx.font = size + 'px monospace';
      for(let i=0;i<drops.length;i++){{
        const text = String.fromCharCode(33 + Math.random() * 94);
        ctx.fillText(text, i*size, drops[i]*size);
        if(drops[i]*size > canvas.height && Math.random() > 0.975) drops[i]=0;
        drops[i]++;
      }}
      requestAnimationFrame(frame);
    }}
    requestAnimationFrame(frame);

    // Fake hacking simulation
    const log = document.getElementById('log');
    function writeLine(txt){{
      const d = document.createElement('div');
      d.textContent = txt;
      log.prepend(d);
    }}

    const fakeMessages = [
      'Escaneando puertos...',
      'Accediendo a base de datos...',
      'Extrayendo credenciales...',
      'Usuario encontrado...',
      'Obteniendo contraseñas de correo...',
      'Obteniendo mensajes de WhatsApp...',
      'Compilando información privada...',
      'Enviando datos a servidor remoto...'
    ];

    let i = 0;
    const interval = setInterval(()=>{{
      if(i < fakeMessages.length){{
        writeLine(fakeMessages[i]);
        i++;
      }}
    }}, 3000);

    // After ~30s show prank modal
    setTimeout(()=>{{
      document.getElementById('modal').classList.add('show');
    }}, 30000);
  </script>
</body>
</html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Railway asigna el puerto automáticamente
    app.run(host="0.0.0.0", port=port)
