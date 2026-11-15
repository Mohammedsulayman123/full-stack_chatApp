import os
import math
from PIL import Image, ImageDraw, ImageFont

def create_pipeline_gif(output_path="assets/devops-pipeline.gif", num_frames=30):
    w, h = 1240, 500
    frames = []

    try:
        font_title = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 20)
        font_sub = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 12)
        font_card_title = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 13)
        font_card_desc = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 11)
        font_code = ImageFont.truetype("C:\\Windows\\Fonts\\consola.ttf", 10)
        font_badge = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 10)
        font_mini = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 9)
    except Exception:
        font_title = ImageFont.load_default()
        font_sub = font_title
        font_card_title = font_title
        font_card_desc = font_title
        font_code = font_title
        font_badge = font_title
        font_mini = font_title

    for frame_idx in range(num_frames):
        t = frame_idx / float(num_frames)
        im = Image.new("RGBA", (w, h), (11, 15, 25, 255))
        draw = ImageDraw.Draw(im)

        # Tech Grid
        for gx in range(0, w, 30):
            draw.line([(gx, 0), (gx, h)], fill=(20, 30, 48, 180), width=1)
        for gy in range(0, h, 30):
            draw.line([(0, gy), (w, gy)], fill=(20, 30, 48, 180), width=1)

        # Header Banner
        pulse_r = int(6 + 3 * math.sin(2 * math.pi * t))
        draw.ellipse([(45 - pulse_r, 38 - pulse_r), (45 + pulse_r, 38 + pulse_r)], fill=(56, 189, 248, 80))
        draw.ellipse([(45 - 5, 38 - 5), (45 + 5, 38 + 5)], fill=(56, 189, 248, 255))
        draw.text((65, 23), "Three-Tier Chat K8s Platform • DevSecOps & Observability Pipeline", fill=(248, 250, 252), font=font_title)
        draw.text((65, 47), "Jenkins CI/CD • SonarQube • Trivy Security • Docker • Kubernetes Helm • HPA Auto-Scaling • Prometheus & Grafana", fill=(148, 163, 184), font=font_sub)

        # Top Badges
        draw.rounded_rectangle([(810, 22), (905, 48)], radius=12, fill=(30, 41, 59), outline=(51, 65, 85))
        draw.ellipse([(822, 32), (830, 40)], fill=(52, 211, 153))
        draw.text((838, 28), "HELM: OK", fill=(52, 211, 153), font=font_badge)

        draw.rounded_rectangle([(915, 22), (1020, 48)], radius=12, fill=(30, 41, 59), outline=(51, 65, 85))
        draw.ellipse([(927, 32), (935, 40)], fill=(56, 189, 248))
        draw.text((943, 28), "HPA ACTIVE", fill=(56, 189, 248), font=font_badge)

        draw.rounded_rectangle([(1030, 22), (1135, 48)], radius=12, fill=(30, 41, 59), outline=(51, 65, 85))
        draw.ellipse([(1042, 32), (1050, 40)], fill=(251, 191, 36))
        draw.text((1058, 28), "99.9% UPTIME", fill=(251, 191, 36), font=font_badge)

        # Stage 1: Developer
        draw.rounded_rectangle([(30, 160), (145, 310)], radius=10, fill=(20, 29, 46), outline=(56, 189, 248), width=2)
        draw.text((45, 175), "Developer", fill=(248, 250, 252), font=font_card_title)
        draw.text((40, 205), "Local Workspace", fill=(148, 163, 184), font=font_card_desc)
        draw.text((40, 225), "git commit & push", fill=(148, 163, 184), font=font_mini)
        draw.rounded_rectangle([(40, 265), (135, 290)], radius=4, fill=(15, 23, 42))
        draw.text((50, 272), "Branch: main", fill=(56, 189, 248), font=font_code)

        # Stage 2: GitHub
        draw.rounded_rectangle([(185, 160), (300, 310)], radius=10, fill=(20, 29, 46), outline=(192, 132, 252), width=2)
        draw.text((200, 175), "GitHub SCM", fill=(248, 250, 252), font=font_card_title)
        draw.text((195, 205), "Webhook Trigger", fill=(148, 163, 184), font=font_card_desc)
        draw.text((195, 225), "Git Repository", fill=(148, 163, 184), font=font_mini)
        draw.rounded_rectangle([(195, 265), (290, 290)], radius=4, fill=(15, 23, 42))
        draw.text((205, 272), "Automated CI", fill=(192, 132, 252), font=font_code)

        # Stage 3: Jenkins DevSecOps Container
        jx, jy, jw, jh = 340, 115, 210, 275
        draw.rounded_rectangle([(jx, jy), (jx + jw, jy + jh)], radius=12, fill=(16, 24, 40), outline=(251, 191, 36), width=2)
        draw.rounded_rectangle([(jx, jy), (jx + jw, jy + 32)], radius=12, fill=(30, 41, 59))
        draw.text((jx + 15, jy + 8), "Jenkins DevSecOps", fill=(251, 191, 36), font=font_card_title)

        # Jenkins Sub-stages
        sub_steps = [
            ("1. SonarQube Scan", "Code Quality & Smells", (56, 189, 248)),
            ("2. Trivy FS Scan", "Vuln & Secret Audit", (248, 113, 113)),
            ("3. Docker Build", "Multi-stage Alpine", (52, 211, 153)),
            ("4. Trivy Image Scan", "CVE HIGH/CRIT Check", (251, 191, 36)),
        ]
        for i, (title, sub, col) in enumerate(sub_steps):
            box_y = jy + 42 + i * 54
            draw.rounded_rectangle([(jx + 12, box_y), (jx + jw - 12, box_y + 46)], radius=6, fill=(15, 23, 42), outline=col, width=1)
            draw.ellipse([(jx + 20, box_y + 18), (jx + 28, box_y + 26)], fill=col)
            draw.text((jx + 34, box_y + 10), title, fill=(248, 250, 252), font=font_badge)
            draw.text((jx + 34, box_y + 26), sub, fill=(148, 163, 184), font=font_mini)

        # Stage 4: Docker Registry
        draw.rounded_rectangle([(590, 160), (705, 310)], radius=10, fill=(20, 29, 46), outline=(56, 189, 248), width=2)
        draw.text((605, 175), "Docker Hub", fill=(248, 250, 252), font=font_card_title)
        draw.text((600, 205), "sulayman12/*", fill=(148, 163, 184), font=font_card_desc)
        draw.text((600, 225), "Secure Alpine Images", fill=(148, 163, 184), font=font_mini)
        draw.rounded_rectangle([(600, 265), (695, 290)], radius=4, fill=(15, 23, 42))
        draw.text((610, 272), "Tag: ${BUILD}", fill=(56, 189, 248), font=font_code)

        # Stage 5: Kubernetes & Helm Cluster (with HPA)
        kx, ky, kw, kh = 745, 110, 270, 285
        draw.rounded_rectangle([(kx, ky), (kx + kw, ky + kh)], radius=12, fill=(12, 19, 34), outline=(59, 130, 246), width=2)
        draw.rounded_rectangle([(kx + 30, ky - 10), (kx + 240, ky + 12)], radius=10, fill=(30, 41, 59), outline=(59, 130, 246))
        draw.text((kx + 45, ky - 6), "Helm Release: chat-app (HPA)", fill=(56, 189, 248), font=font_badge)

        # Pod cards inside K8s
        draw.rounded_rectangle([(kx + 12, ky + 25), (kx + kw - 12, ky + 90)], radius=6, fill=(20, 29, 46), outline=(52, 211, 153), width=1)
        draw.text((kx + 22, ky + 34), "Frontend Pods (HPA 2-5)", fill=(248, 250, 252), font=font_badge)
        draw.text((kx + 22, ky + 50), "React 18 + DaisyUI • Port: 80", fill=(148, 163, 184), font=font_mini)
        draw.text((kx + 22, ky + 66), "Auto-scales on CPU > 70%", fill=(52, 211, 153), font=font_code)

        draw.rounded_rectangle([(kx + 12, ky + 105), (kx + kw - 12, ky + 180)], radius=6, fill=(20, 29, 46), outline=(251, 191, 36), width=1)
        draw.text((kx + 22, ky + 114), "Backend API Pods (HPA 2-10)", fill=(248, 250, 252), font=font_badge)
        draw.text((kx + 22, ky + 130), "Node.js + Socket.io • Port: 5001", fill=(148, 163, 184), font=font_mini)
        draw.text((kx + 22, ky + 146), "Auto-scales on CPU/Mem > 75%", fill=(251, 191, 36), font=font_code)
        draw.text((kx + 22, ky + 160), "Metrics Exporter: /metrics", fill=(56, 189, 248), font=font_mini)

        draw.rounded_rectangle([(kx + 12, ky + 195), (kx + kw - 12, ky + 265)], radius=6, fill=(20, 29, 46), outline=(16, 185, 129), width=1)
        draw.text((kx + 22, ky + 204), "MongoDB Stateful Pod", fill=(248, 250, 252), font=font_badge)
        draw.text((kx + 22, ky + 220), "Port: 27017 • Persistence Claim", fill=(148, 163, 184), font=font_mini)
        draw.text((kx + 22, ky + 238), "PVC: mongodb-pvc (1Gi PV)", fill=(16, 185, 129), font=font_code)

        # Stage 6: Observability (Prometheus & Grafana)
        ox, oy, ow, oh = 1055, 130, 155, 245
        draw.rounded_rectangle([(ox, oy), (ox + ow, oy + oh)], radius=12, fill=(20, 29, 46), outline=(234, 88, 12), width=2)
        draw.text((ox + 15, oy + 15), "Observability", fill=(251, 146, 60), font=font_card_title)
        draw.text((ox + 15, oy + 38), "Prometheus & Grafana", fill=(248, 250, 252), font=font_badge)

        draw.rounded_rectangle([(ox + 10, oy + 65), (ox + ow - 10, oy + 135)], radius=6, fill=(15, 23, 42), outline=(234, 88, 12), width=1)
        draw.ellipse([(ox + 20, oy + 80), (ox + 28, oy + 88)], fill=(234, 88, 12))
        draw.text((ox + 35, oy + 76), "Prometheus", fill=(248, 250, 252), font=font_badge)
        draw.text((ox + 20, oy + 95), "Scrapes /metrics 15s", fill=(148, 163, 184), font=font_mini)
        draw.text((ox + 20, oy + 112), "Alerts: 99.9% SLA", fill=(234, 88, 12), font=font_code)

        draw.rounded_rectangle([(ox + 10, oy + 150), (ox + ow - 10, oy + 225)], radius=6, fill=(15, 23, 42), outline=(251, 191, 36), width=1)
        draw.ellipse([(ox + 20, oy + 165), (ox + 28, oy + 173)], fill=(251, 191, 36))
        draw.text((ox + 35, oy + 161), "Grafana", fill=(248, 250, 252), font=font_badge)
        draw.text((ox + 20, oy + 180), "Live Dashboard", fill=(148, 163, 184), font=font_mini)
        draw.text((ox + 20, oy + 198), "Active Sockets & Latency", fill=(251, 191, 36), font=font_mini)

        # Static connecting lines
        draw.line([(145, 235), (185, 235)], fill=(51, 65, 85), width=2)
        draw.line([(300, 235), (340, 235)], fill=(51, 65, 85), width=2)
        draw.line([(550, 235), (590, 235)], fill=(51, 65, 85), width=2)
        draw.line([(705, 235), (745, 235)], fill=(51, 65, 85), width=2)
        draw.line([(1015, 235), (1055, 235)], fill=(51, 65, 85), width=2)

        # Helper moving dot function
        def draw_dot(p_start, p_end, progress, color, size=6):
            px = p_start[0] + (p_end[0] - p_start[0]) * progress
            py = p_start[1] + (p_end[1] - p_start[1]) * progress
            glow = size + 4
            draw.ellipse([(px - glow, py - glow), (px + glow, py + glow)], fill=(*color, 80))
            draw.ellipse([(px - size, py - size), (px + size, py + size)], fill=(*color, 255))
            draw.ellipse([(px - size // 2, py - size // 2), (px + size // 2, py + size // 2)], fill=(255, 255, 255, 255))

        # Dot 1: Dev -> Git
        draw_dot((145, 235), (185, 235), t % 1.0, (56, 189, 248))

        # Dot 2: Git -> Jenkins
        draw_dot((300, 235), (340, 235), (t + 0.25) % 1.0, (192, 132, 252))

        # Dot 3: Jenkins internal progression
        step_idx = int(t * 4) % 4
        jdot_y = jy + 60 + step_idx * 54
        draw.ellipse([(jx + 24 - 4, jdot_y - 4), (jx + 24 + 4, jdot_y + 4)], fill=(255, 255, 255))

        # Dot 4: Jenkins -> Docker Hub
        draw_dot((550, 235), (590, 235), (t + 0.5) % 1.0, (251, 191, 36))

        # Dot 5: Docker Hub -> Helm K8s Deploy
        draw_dot((705, 235), (745, 235), (t + 0.75) % 1.0, (56, 189, 248))

        # Dot 6: K8s Backend -> Prometheus Metrics Scraping (Observability Loop)
        draw_dot((1015, 235), (1055, 235), (t + 0.4) % 1.0, (234, 88, 12))

        # Footer Legend
        draw.ellipse([(40, 465), (48, 473)], fill=(56, 189, 248))
        draw.text((55, 462), "Git & SCM Delivery", fill=(148, 163, 184), font=font_sub)

        draw.ellipse([(200, 465), (208, 473)], fill=(251, 191, 36))
        draw.text((215, 462), "DevSecOps (SonarQube & Trivy)", fill=(148, 163, 184), font=font_sub)

        draw.ellipse([(440, 465), (448, 473)], fill=(52, 211, 153))
        draw.text((455, 462), "Kubernetes Helm & HPA Scaling", fill=(148, 163, 184), font=font_sub)

        draw.ellipse([(700, 465), (708, 473)], fill=(234, 88, 12))
        draw.text((715, 462), "Prometheus & Grafana Observability (99.9% Uptime)", fill=(148, 163, 184), font=font_sub)

        frame_rgb = im.convert("RGB")
        frame_p = frame_rgb.convert("P", palette=Image.ADAPTIVE, colors=128)
        frames.append(frame_p)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    frames[0].save(
        output_path,
        save_all=True,
        append_images=frames[1:],
        duration=60,
        loop=0,
        optimize=True
    )
    print(f"Created updated DevSecOps pipeline animated GIF at {output_path} ({os.path.getsize(output_path)} bytes)")

create_pipeline_gif()
