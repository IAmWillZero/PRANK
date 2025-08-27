from flask import Flask
app = Flask(__name__)

visitas = 0

@app.route("/")
def home():
    global visitas
    visitas += 1
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
      background:#000;
      color:#00ff6a;
      font-family:monospace, system-ui, monospace;
      overflow:hidden;
    }}

    .matrix{{position:fixed;inset:0;z-index:0;}}
    canvas{{width:100%;height:100%;display:block}}

    .panel{{position:relative;z-index:2;padding:32px;max-width:1000px;
      margin:40px auto;background:rgba(0,0,0,0.45);
      border:1px solid rgba(0,255,106,0.08);
      box-shadow:0 8px 40px rgba(0,0,0,0.7);
      border-radius:10px;backdrop-filter:blur(4px)}}

    h1{{font-size:36px;letter-spacing:2px;color:#ff2d2d;
      text-shadow:0 0 12px rgba(255,45,45,0.25)}}

    .log{{margin-top:18px;background:rgba(0,0,0,0.6);padding:14px;
      border-radius:6px;height:320px;overflow:auto;
      border:1px dashed rgba(0,255,106,0.06)}}
    .log > div{{font-size:14px;line-height:1.45}}

    .modal{{position:fixed;inset:0;display:flex;align-items:center;
      justify-content:center;padding:24px;z-index:9;visibility:hidden;
      opacity:0;transition:all .25s}}
    .modal.show{{visibility:visible;opacity:1}}
    .modal .card{{background:#050505;padding:20px;border-radius:10px;
      max-width:760px;border:1px solid rgba(255,0,0,0.08)}}
    .modal h2{{color:#ffbcbc}}
    .modal p{{color:#d6ffd7;margin-top:8px}}

    footer{{position:fixed;left:12px;bottom:12px;z-index:3;
      font-size:13px;color:rgba(255,255,255,0.2)}}
  </style>
</head>
<body>
  <div class="matrix"><canvas id="matrixCanvas"></canvas></div>

  <div class="panel" role="main">
    <h1>!!! SYSTEM BREACH !!!</h1>
    <p>Visitas: {visitas}</p>
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
    app.run(host="0.0.0.0", port=8000, debug=True)
