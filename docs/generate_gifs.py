import os
import math
from PIL import Image, ImageDraw, ImageFont

def create_pipeline_gif(output_path="assets/devops-pipeline.gif", num_frames=30):
    w, h = 1200, 480
    frames = []

    try:
        font_title = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 20)
        font_sub = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 12)
        font_card_title = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 14)
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

    # Predefined positions
    stages = [
        {"x": 40, "y": 170, "w": 140, "h": 150, "title": "Developer", "sub": "Local Workspace", "tag": "git push", "color": (56, 189, 248)},
        {"x": 250, "y": 170, "w": 140, "h": 150, "title": "GitHub Repo", "sub": "branch: master", "tag": "webhook trigger", "color": (192, 132, 252)},
        {"x": 460, "y": 135, "w": 170, "h": 220, "title": "Jenkins Pipeline", "sub": "Automated CI/CD", "tag": "Jenkinsfile", "color": (251, 191, 36)},
        {"x": 700, "y": 170, "w": 140, "h": 150, "title": "Docker Hub", "sub": "sulayman12/*", "tag": "tag: latest", "color": (56, 189, 248)},
    ]

    for frame_idx in range(num_frames):
        t = frame_idx / float(num_frames)
        im = Image.new("RGBA", (w, h), (11, 15, 25, 255))
        draw = ImageDraw.Draw(im)

        # Draw tech grid
        for gx in range(0, w, 30):
            draw.line([(gx, 0), (gx, h)], fill=(22, 32, 50, 180), width=1)
        for gy in range(0, h, 30):
            draw.line([(0, gy), (w, gy)], fill=(22, 32, 50, 180), width=1)

        # Header Banner
        pulse_r = int(6 + 3 * math.sin(2 * math.pi * t))
        draw.ellipse([(45 - pulse_r, 38 - pulse_r), (45 + pulse_r, 38 + pulse_r)], fill=(56, 189, 248, 80))
        draw.ellipse([(45 - 5, 38 - 5), (45 + 5, 38 + 5)], fill=(56, 189, 248, 255))
        draw.text((65, 25), "DevOps CI/CD Automation & Kubernetes Deployment Pipeline", fill=(248, 250, 252), font=font_title)
        draw.text((65, 48), "Live Moving-Dot Telemetry • Automated Git Commit, Smoke Test, Multi-Stage Build & Cluster Rollout", fill=(148, 163, 184), font=font_sub)

        # Status Badges
        draw.rounded_rectangle([(870, 25), (965, 50)], radius=12, fill=(30, 41, 59), outline=(51, 65, 85))
        draw.ellipse([(882, 35), (890, 43)], fill=(52, 211, 153))
        draw.text((898, 31), "PIPELINE: OK", fill=(52, 211, 153), font=font_badge)

        draw.rounded_rectangle([(975, 25), (1075, 50)], radius=12, fill=(30, 41, 59), outline=(51, 65, 85))
        draw.ellipse([(987, 35), (995, 43)], fill=(56, 189, 248))
        draw.text((1003, 31), "K8S CLUSTER", fill=(56, 189, 248), font=font_badge)

        draw.rounded_rectangle([(1085, 25), (1160, 50)], radius=12, fill=(30, 41, 59), outline=(51, 65, 85))
        draw.ellipse([(1097, 35), (1105, 43)], fill=(251, 191, 36))
        draw.text((1113, 31), "LIVE", fill=(251, 191, 36), font=font_badge)

        # Draw Main Stage Cards
        for s in stages:
            draw.rounded_rectangle([(s["x"], s["y"]), (s["x"] + s["w"], s["y"] + s["h"])], radius=12, fill=(20, 29, 46, 240), outline=s["color"], width=2)
            
            # Pulse beacon in node
            cx = s["x"] + 25
            cy = s["y"] + 25
            node_pulse = int(5 + 3 * math.sin(2 * math.pi * t + s["x"]))
            draw.ellipse([(cx - node_pulse, cy - node_pulse), (cx + node_pulse, cy + node_pulse)], fill=(*s["color"], 60))
            draw.ellipse([(cx - 4, cy - 4), (cx + 4, cy + 4)], fill=s["color"])

            draw.text((s["x"] + 45, s["y"] + 16), s["title"], fill=(241, 245, 249), font=font_card_title)
            draw.text((s["x"] + 15, s["y"] + 55), s["sub"], fill=(148, 163, 184), font=font_card_desc)

            # Badge pill
            draw.rounded_rectangle([(s["x"] + 15, s["y"] + s["h"] - 35), (s["x"] + s["w"] - 15, s["y"] + s["h"] - 15)], radius=6, fill=(15, 23, 42), outline=(51, 65, 85))
            draw.text((s["x"] + 25, s["y"] + s["h"] - 32), s["tag"], fill=s["color"], font=font_code)

        # Jenkins Sub-Stages
        jx = 460
        jy = 135
        # Sub-box 1: Checkout
        draw.rounded_rectangle([(jx + 15, jy + 50), (jx + 155, jy + 90)], radius=6, fill=(15, 23, 42), outline=(51, 65, 85))
        draw.ellipse([(jx + 25, jy + 67), (jx + 33, jy + 75)], fill=(52, 211, 153))
        draw.text((jx + 40, jy + 58), "1. Checkout", fill=(248, 250, 252), font=font_badge)
        draw.text((jx + 40, jy + 72), "Fetch latest master", fill=(148, 163, 184), font=font_mini)

        # Sub-box 2: Smoke Test
        draw.rounded_rectangle([(jx + 15, jy + 98), (jx + 155, jy + 138)], radius=6, fill=(15, 23, 42), outline=(51, 65, 85))
        draw.ellipse([(jx + 25, jy + 115), (jx + 33, jy + 123)], fill=(56, 189, 248))
        draw.text((jx + 40, jy + 106), "2. Smoke Test", fill=(248, 250, 252), font=font_badge)
        draw.text((jx + 40, jy + 120), "curl /health verify", fill=(148, 163, 184), font=font_mini)

        # Sub-box 3: Docker Build
        draw.rounded_rectangle([(jx + 15, jy + 146), (jx + 155, jy + 196)], radius=6, fill=(15, 23, 42), outline=(251, 191, 36), width=1)
        draw.ellipse([(jx + 25, jy + 167), (jx + 33, jy + 175)], fill=(251, 191, 36))
        draw.text((jx + 40, jy + 155), "3. Docker Build", fill=(248, 250, 252), font=font_badge)
        draw.text((jx + 40, jy + 169), "Multi-stage alpine", fill=(148, 163, 184), font=font_mini)
        draw.text((jx + 40, jy + 181), "docker-compose", fill=(251, 191, 36), font=font_mini)

        # Kubernetes Cluster Box
        kx = 900
        ky = 120
        kw = 260
        kh = 250
        draw.rounded_rectangle([(kx, ky), (kx + kw, ky + kh)], radius=14, fill=(12, 19, 34, 230), outline=(59, 130, 246), width=2)
        # Namespace badge
        draw.rounded_rectangle([(kx + 35, ky - 10), (kx + 225, ky + 12)], radius=11, fill=(30, 41, 59), outline=(59, 130, 246))
        draw.text((kx + 50, ky - 6), "K8s Namespace: chat-app", fill=(56, 189, 248), font=font_badge)

        # Ingress
        draw.rounded_rectangle([(kx + 15, ky + 30), (kx + 85, ky + 120)], radius=8, fill=(20, 29, 46), outline=(56, 189, 248))
        draw.text((kx + 25, ky + 45), "Ingress", fill=(248, 250, 252), font=font_badge)
        draw.text((kx + 22, ky + 65), "Nginx", fill=(148, 163, 184), font=font_mini)
        draw.text((kx + 18, ky + 85), "chat-tws", fill=(56, 189, 248), font=font_mini)

        # Frontend Pod
        draw.rounded_rectangle([(kx + 105, ky + 25), (kx + 245, ky + 85)], radius=8, fill=(20, 29, 46), outline=(52, 211, 153), width=1)
        draw.ellipse([(kx + 115, ky + 38), (kx + 123, ky + 46)], fill=(52, 211, 153))
        draw.text((kx + 130, ky + 34), "Frontend Pod", fill=(248, 250, 252), font=font_badge)
        draw.text((kx + 115, ky + 52), "React 18 + DaisyUI", fill=(148, 163, 184), font=font_mini)
        draw.text((kx + 115, ky + 68), "Port: 80 / ClusterIP", fill=(52, 211, 153), font=font_code)

        # Backend Pod
        draw.rounded_rectangle([(kx + 105, ky + 100), (kx + 245, ky + 160)], radius=8, fill=(20, 29, 46), outline=(251, 191, 36), width=1)
        draw.ellipse([(kx + 115, ky + 113), (kx + 123, ky + 121)], fill=(251, 191, 36))
        draw.text((kx + 130, ky + 109), "Backend Pod", fill=(248, 250, 252), font=font_badge)
        draw.text((kx + 115, ky + 127), "Node + Socket.io", fill=(148, 163, 184), font=font_mini)
        draw.text((kx + 115, ky + 143), "Port: 5001 / Health", fill=(251, 191, 36), font=font_code)

        # MongoDB Pod
        draw.rounded_rectangle([(kx + 105, ky + 175), (kx + 245, ky + 235)], radius=8, fill=(20, 29, 46), outline=(16, 185, 129), width=1)
        draw.ellipse([(kx + 115, ky + 188), (kx + 123, ky + 196)], fill=(16, 185, 129))
        draw.text((kx + 130, ky + 184), "MongoDB (PVC)", fill=(248, 250, 252), font=font_badge)
        draw.text((kx + 115, ky + 202), "Port: 27017 / Data", fill=(148, 163, 184), font=font_mini)
        draw.text((kx + 115, ky + 218), "PVC: mongodb-pvc", fill=(16, 185, 129), font=font_code)

        # Static connecting dashed wires
        connectors = [
            ((180, 245), (250, 245)),
            ((390, 245), (460, 245)),
            ((630, 245), (700, 245)),
            ((840, 245), (915, 245)),
            ((985, 175), (1005, 155)),
            ((985, 245), (1005, 230)),
            ((1175, 245), (1175, 295)),
        ]
        for p1, p2 in connectors:
            draw.line([p1, p2], fill=(51, 65, 85), width=2)

        # Function to draw moving glowing dot
        def draw_moving_dot(p_start, p_end, progress, color, size=6):
            px = p_start[0] + (p_end[0] - p_start[0]) * progress
            py = p_start[1] + (p_end[1] - p_start[1]) * progress
            glow = size + 4
            draw.ellipse([(px - glow, py - glow), (px + glow, py + glow)], fill=(*color, 80))
            draw.ellipse([(px - size, py - size), (px + size, py + size)], fill=(*color, 255))
            draw.ellipse([(px - size // 2, py - size // 2), (px + size // 2, py + size // 2)], fill=(255, 255, 255, 255))

        # Dot 1: Dev -> Git
        draw_moving_dot((180, 245), (250, 245), (t) % 1.0, (56, 189, 248))
        draw_moving_dot((180, 245), (250, 245), (t + 0.5) % 1.0, (56, 189, 248), size=4)

        # Dot 2: Git -> Jenkins
        draw_moving_dot((390, 245), (460, 245), (t + 0.2) % 1.0, (192, 132, 252))

        # Dot 3: Jenkins -> Docker Hub
        draw_moving_dot((630, 245), (700, 245), (t + 0.5) % 1.0, (251, 191, 36))

        # Dot 4: Docker Hub -> K8s Ingress
        draw_moving_dot((840, 245), (915, 245), (t + 0.7) % 1.0, (56, 189, 248))

        # Dot 5: Ingress -> Frontend Pod
        draw_moving_dot((kx + 85, ky + 65), (kx + 105, ky + 55), (t + 0.1) % 1.0, (52, 211, 153))

        # Dot 6: Ingress -> Backend Pod
        draw_moving_dot((kx + 85, ky + 85), (kx + 105, ky + 130), (t + 0.3) % 1.0, (251, 191, 36))

        # Dot 7: Backend Pod -> Mongo Pod
        draw_moving_dot((kx + 175, ky + 160), (kx + 175, ky + 175), (t + 0.6) % 1.0, (16, 185, 129))

        # Legend Footer
        draw.ellipse([(60, 445), (68, 453)], fill=(56, 189, 248))
        draw.text((75, 442), "Git & Deployment Artifacts", fill=(148, 163, 184), font=font_sub)

        draw.ellipse([(260, 445), (268, 453)], fill=(192, 132, 252))
        draw.text((275, 442), "Webhook Trigger", fill=(148, 163, 184), font=font_sub)

        draw.ellipse([(430, 445), (438, 453)], fill=(251, 191, 36))
        draw.text((445, 442), "Container Build / Test", fill=(148, 163, 184), font=font_sub)

        draw.ellipse([(630, 445), (638, 453)], fill=(52, 211, 153))
        draw.text((645, 442), "Kubernetes Pod Routing & Sync", fill=(148, 163, 184), font=font_sub)

        # Convert RGBA to P mode for GIF optimization
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
    print(f"Created animated GIF at {output_path} ({os.path.getsize(output_path)} bytes)")

create_pipeline_gif()


def create_architecture_gif(output_path="assets/architecture-diagram.gif", num_frames=30):
    w, h = 1200, 520
    frames = []

    try:
        font_title = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 20)
        font_sub = ImageFont.truetype("C:\\Windows\\Fonts\\segoeui.ttf", 12)
        font_card_title = ImageFont.truetype("C:\\Windows\\Fonts\\segoeuib.ttf", 14)
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
        im = Image.new("RGBA", (w, h), (9, 13, 22, 255))
        draw = ImageDraw.Draw(im)

        # Tech Grid
        for gx in range(0, w, 30):
            draw.line([(gx, 0), (gx, h)], fill=(20, 28, 44, 180), width=1)
        for gy in range(0, h, 30):
            draw.line([(0, gy), (w, gy)], fill=(20, 28, 44, 180), width=1)

        # Header
        pulse_r = int(6 + 3 * math.sin(2 * math.pi * t))
        draw.ellipse([(45 - pulse_r, 38 - pulse_r), (45 + pulse_r, 38 + pulse_r)], fill=(74, 222, 128, 80))
        draw.ellipse([(45 - 5, 38 - 5), (45 + 5, 38 + 5)], fill=(74, 222, 128, 255))
        draw.text((65, 25), "Real-Time Application Architecture & Data Pipeline", fill=(248, 250, 252), font=font_title)
        draw.text((65, 48), "Bi-Directional WebSocket Streaming • REST API Microservices • MongoDB Persistence • Cloudinary Media", fill=(148, 163, 184), font=font_sub)

        # Client A (Alice)
        draw.rounded_rectangle([(40, 100), (200, 220)], radius=12, fill=(20, 29, 46), outline=(56, 189, 248), width=2)
        draw.ellipse([(55, 115), (71, 131)], fill=(56, 189, 248))
        draw.text((80, 115), "Client A (Alice)", fill=(248, 250, 252), font=font_card_title)
        draw.text((55, 140), "● Online / Connected", fill=(74, 222, 128), font=font_badge)
        draw.text((55, 160), "React 18 + Vite", fill=(148, 163, 184), font=font_card_desc)
        draw.text((55, 175), "Zustand State Store", fill=(148, 163, 184), font=font_card_desc)
        draw.rounded_rectangle([(55, 192), (185, 210)], radius=4, fill=(15, 23, 42))
        draw.text((70, 195), "Socket.io-client", fill=(56, 189, 248), font=font_code)

        # Client B (Bob)
        draw.rounded_rectangle([(40, 310), (200, 430)], radius=12, fill=(20, 29, 46), outline=(192, 132, 252), width=2)
        draw.ellipse([(55, 325), (71, 341)], fill=(192, 132, 252))
        draw.text((80, 325), "Client B (Bob)", fill=(248, 250, 252), font=font_card_title)
        draw.text((55, 350), "● Online / Connected", fill=(74, 222, 128), font=font_badge)
        draw.text((55, 370), "React 18 + Vite", fill=(148, 163, 184), font=font_card_desc)
        draw.text((55, 385), "Tailwind + DaisyUI", fill=(148, 163, 184), font=font_card_desc)
        draw.rounded_rectangle([(55, 402), (185, 420)], radius=4, fill=(15, 23, 42))
        draw.text((70, 405), "Socket.io-client", fill=(192, 132, 252), font=font_code)

        # Nginx Reverse Proxy
        draw.rounded_rectangle([(330, 195), (450, 335)], radius=12, fill=(20, 29, 46), outline=(16, 185, 129), width=2)
        draw.text((355, 215), "NGINX", fill=(16, 185, 129), font=font_card_title)
        draw.text((345, 240), "Reverse Proxy", fill=(248, 250, 252), font=font_badge)
        draw.text((345, 258), "Ingress Route", fill=(148, 163, 184), font=font_mini)
        draw.rounded_rectangle([(345, 275), (435, 295)], radius=4, fill=(15, 23, 42))
        draw.text((355, 280), "Port: 80 / 8080", fill=(16, 185, 129), font=font_code)
        draw.rounded_rectangle([(345, 302), (435, 320)], radius=4, fill=(6, 78, 59))
        draw.text((350, 306), "WS UPGRADE", fill=(167, 243, 208), font=font_badge)

        # Backend Engine Box (Node.js + Express)
        bx = 560
        by = 145
        bw = 280
        bh = 250
        draw.rounded_rectangle([(bx, by), (bx + bw, by + bh)], radius=14, fill=(20, 29, 46), outline=(59, 130, 246), width=2)
        draw.rounded_rectangle([(bx, by), (bx + bw, by + 36)], radius=14, fill=(30, 41, 59))
        draw.text((bx + 15, by + 10), "Node.js Express & Socket.io", fill=(248, 250, 252), font=font_card_title)
        draw.text((bx + 205, by + 12), "PORT: 5001", fill=(56, 189, 248), font=font_code)

        # Sub 1: Auth
        draw.rounded_rectangle([(bx + 15, by + 48), (bx + 265, by + 95)], radius=6, fill=(15, 23, 42), outline=(51, 65, 85))
        draw.ellipse([(bx + 25, by + 65), (bx + 33, by + 73)], fill=(56, 189, 248))
        draw.text((bx + 40, by + 56), "Auth & JWT Verification", fill=(248, 250, 252), font=font_badge)
        draw.text((bx + 40, by + 72), "HTTP-only cookie + bcrypt hash", fill=(148, 163, 184), font=font_mini)

        # Sub 2: Socket.io
        draw.rounded_rectangle([(bx + 15, by + 105), (bx + 265, by + 165)], radius=6, fill=(15, 23, 42), outline=(74, 222, 128), width=1)
        draw.ellipse([(bx + 25, by + 125), (bx + 33, by + 133)], fill=(74, 222, 128))
        draw.text((bx + 40, by + 115), "Socket.io Engine", fill=(74, 222, 128), font=font_badge)
        draw.text((bx + 40, by + 130), "userSocketMap: { userId -> socketId }", fill=(203, 213, 225), font=font_mini)
        draw.text((bx + 40, by + 144), "getOnlineUsers • newMessage broadcast", fill=(148, 163, 184), font=font_mini)

        # Sub 3: Message Router
        draw.rounded_rectangle([(bx + 15, by + 175), (bx + 265, by + 225)], radius=6, fill=(15, 23, 42), outline=(51, 65, 85))
        draw.ellipse([(bx + 25, by + 192), (bx + 33, by + 200)], fill=(251, 191, 36))
        draw.text((bx + 40, by + 183), "Message & Health Controller", fill=(248, 250, 252), font=font_badge)
        draw.text((bx + 40, by + 199), "/api/messages • /health endpoint", fill=(148, 163, 184), font=font_mini)

        # MongoDB Box
        draw.rounded_rectangle([(950, 110), (1160, 240)], radius=12, fill=(20, 29, 46), outline=(16, 185, 129), width=2)
        draw.ellipse([(965, 125), (981, 141)], fill=(16, 185, 129))
        draw.text((990, 123), "MongoDB Database", fill=(248, 250, 252), font=font_card_title)
        draw.text((965, 150), "Port: 27017 • Replica / PV", fill=(52, 211, 153), font=font_badge)
        draw.text((965, 172), "• users: { name, email, pic }", fill=(148, 163, 184), font=font_mini)
        draw.text((965, 188), "• messages: { sender, text }", fill=(148, 163, 184), font=font_mini)
        draw.rounded_rectangle([(965, 205), (1145, 225)], radius=4, fill=(15, 23, 42))
        draw.text((980, 210), "K8s PVC: mongodb-pvc", fill=(16, 185, 129), font=font_code)

        # Cloudinary CDN Box
        draw.rounded_rectangle([(950, 290), (1160, 420)], radius=12, fill=(20, 29, 46), outline=(56, 189, 248), width=2)
        draw.ellipse([(965, 305), (981, 321)], fill=(56, 189, 248))
        draw.text((990, 303), "Cloudinary CDN", fill=(248, 250, 252), font=font_card_title)
        draw.text((965, 330), "Cloud Media Storage", fill=(56, 189, 248), font=font_badge)
        draw.text((965, 352), "• User Profile Avatars", fill=(148, 163, 184), font=font_mini)
        draw.text((965, 368), "• Chat Shared Photos", fill=(148, 163, 184), font=font_mini)
        draw.rounded_rectangle([(965, 385), (1145, 405)], radius=4, fill=(15, 23, 42))
        draw.text((980, 390), "Secure Media API", fill=(56, 189, 248), font=font_code)

        # Static Connecting lines
        draw.line([(200, 160), (330, 235)], fill=(51, 65, 85), width=2)
        draw.line([(200, 370), (330, 295)], fill=(51, 65, 85), width=2)
        draw.line([(450, 265), (560, 265)], fill=(51, 65, 85), width=2)
        draw.line([(840, 220), (950, 175)], fill=(51, 65, 85), width=2)
        draw.line([(840, 310), (950, 355)], fill=(51, 65, 85), width=2)

        # Helper moving dot function
        def draw_dot(p_start, p_end, progress, color, size=6):
            px = p_start[0] + (p_end[0] - p_start[0]) * progress
            py = p_start[1] + (p_end[1] - p_start[1]) * progress
            glow = size + 4
            draw.ellipse([(px - glow, py - glow), (px + glow, py + glow)], fill=(*color, 80))
            draw.ellipse([(px - size, py - size), (px + size, py + size)], fill=(*color, 255))
            draw.ellipse([(px - size // 2, py - size // 2), (px + size // 2, py + size // 2)], fill=(255, 255, 255, 255))

        # 1. Alice Sends Message -> Nginx
        draw_dot((200, 160), (330, 235), t % 1.0, (74, 222, 128))

        # 2. Nginx -> Backend Engine
        draw_dot((450, 265), (560, 265), (t + 0.3) % 1.0, (74, 222, 128))

        # 3. Backend -> MongoDB
        draw_dot((840, 220), (950, 175), (t + 0.6) % 1.0, (16, 185, 129))

        # 4. Backend -> Cloudinary
        draw_dot((840, 310), (950, 355), (t + 0.4) % 1.0, (56, 189, 248))

        # 5. Broadcast back to Bob (Nginx -> Bob)
        draw_dot((330, 295), (200, 370), (t + 0.7) % 1.0, (74, 222, 128))

        # Legend Footer
        draw.ellipse([(60, 480), (68, 488)], fill=(74, 222, 128))
        draw.text((75, 477), "Real-Time WebSocket Message Stream (Instant Delivery)", fill=(148, 163, 184), font=font_sub)

        draw.ellipse([(440, 480), (448, 488)], fill=(16, 185, 129))
        draw.text((455, 477), "MongoDB Persistence Storage", fill=(148, 163, 184), font=font_sub)

        draw.ellipse([(700, 480), (708, 488)], fill=(56, 189, 248))
        draw.text((715, 477), "REST Auth & Cloudinary Asset Pipeline", fill=(148, 163, 184), font=font_sub)

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
    print(f"Created architecture animated GIF at {output_path} ({os.path.getsize(output_path)} bytes)")

create_architecture_gif()
