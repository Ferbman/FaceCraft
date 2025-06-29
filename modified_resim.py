import sys
import os
import torch
import legacy
import dnnlib
import numpy as np
from PIL import Image
from labels import metni_etiketle
import random

# ---- Komut satırından argümanları al ----
if len(sys.argv) < 3:
    print("Kullanım: python modified_resim.py 'metin' output_path.png")
    sys.exit(1)

text = sys.argv[1]
output_path = sys.argv[2]

# ---- Model ve ayarlar ----
network_pkl = 'network-snapshot-001300.pkl'  # Eğitilmiş StyleGAN3 model dosyası
device = torch.device('cpu')
seed = 34 #random.randint(30, 50)

# ---- Metni etiketlere dönüştür ----
labels = metni_etiketle(text)  # Zaten [-1, 1] formatında liste
print(f"Kullanılan etiketler: {labels}")

# ---- Modeli yükle ----
print(f"Using device: {device}")
print(f"Loading network from {network_pkl}...")
with dnnlib.util.open_url(network_pkl) as f:
    G = legacy.load_network_pkl(f)['G_ema'].to(device)

# ---- Latent vektörü oluştur ----
print(f"Generating random latent vector with seed {seed}...")
z = torch.from_numpy(np.random.RandomState(seed).randn(1, G.z_dim)).to(device)
c = torch.tensor(labels, dtype=torch.float32, device=device).unsqueeze(0)

# ---- Görsel oluştur ----
print(f"Generating image with label: {labels}")
with torch.no_grad():
    img = G(z, c, truncation_psi=1, noise_mode='const')

# ---- Görseli kaydet ----
img = (img.clamp(-1, 1) + 1) * (255 / 2)
img = img.permute(0, 2, 3, 1)[0].cpu().numpy().astype(np.uint8)

os.makedirs(os.path.dirname(output_path), exist_ok=True)
Image.fromarray(img).save(output_path)
print(f"Image saved to {output_path}.")
