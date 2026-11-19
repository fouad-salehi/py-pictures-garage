import cv2
import numpy as np


def oil_painting(img):
    return cv2.stylization(img, sigma_s=60, sigma_r=0.45)


def cartoon(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(
        gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY, 9, 9
    )
    color = cv2.bilateralFilter(img, 9, 300, 300)
    return cv2.bitwise_and(color, color, mask=edges)


def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (21, 21), 0)
    inv_blur = 255 - blur
    sketch = cv2.divide(gray, inv_blur, scale=256.0)
    return cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)


def watercolor(img):
    result = img.copy()
    for _ in range(3):
        result = cv2.bilateralFilter(result, 9, 75, 75)
    hsv = cv2.cvtColor(result, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.4, 0, 255)
    result = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
    return cv2.GaussianBlur(result, (3, 3), 0)


def vintage_film(img):
    result = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
    sepia = np.array([[0.272, 0.534, 0.131],
                      [0.349, 0.686, 0.168],
                      [0.393, 0.769, 0.189]])
    sepia_img = cv2.transform(result, sepia)
    sepia_img = np.clip(sepia_img, 0, 255).astype(np.uint8)
    noise = np.random.normal(0, 8, sepia_img.shape).astype(np.int16)
    noisy = np.clip(sepia_img.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    h, w = noisy.shape[:2]
    kernel_x = cv2.getGaussianKernel(w, w * 0.5)
    kernel_y = cv2.getGaussianKernel(h, h * 0.5)
    mask = kernel_y @ kernel_x.T
    mask = mask / mask.max()
    mask = np.dstack([mask] * 3)
    return (noisy * mask).astype(np.uint8)


def hdr_effect(img):
    return cv2.detailEnhance(img, sigma_s=12, sigma_r=0.15)


def sharpen(img):
    gaussian = cv2.GaussianBlur(img, (0, 0), 3)
    return cv2.addWeighted(img, 1.6, gaussian, -0.6, 0)


def cool_tone(img):
    result = img.astype(np.float32)
    result[:, :, 0] = np.clip(result[:, :, 0] * 1.15, 0, 255)
    result[:, :, 2] = np.clip(result[:, :, 2] * 0.88, 0, 255)
    return result.astype(np.uint8)


def warm_tone(img):
    result = img.astype(np.float32)
    result[:, :, 2] = np.clip(result[:, :, 2] * 1.15, 0, 255)
    result[:, :, 0] = np.clip(result[:, :, 0] * 0.88, 0, 255)
    return result.astype(np.uint8)


def noir_bw(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    return cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)


def vivid(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.6, 0, 255)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * 1.08, 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)


def blur_bokeh(img):
    h, w = img.shape[:2]
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.circle(mask, (w // 2, h // 2), min(w, h) // 3, 255, -1)
    mask = cv2.GaussianBlur(mask, (0, 0), min(w, h) // 8)
    mask = np.dstack([mask / 255.0] * 3)
    blurred = cv2.GaussianBlur(img, (0, 0), 12)
    return (img * mask + blurred * (1 - mask)).astype(np.uint8)


EFFECTS = {
    "Oil Painting": oil_painting,
    "Cartoon": cartoon,
    "Pencil Sketch": pencil_sketch,
    "Watercolor": watercolor,
    "Vintage Film": vintage_film,
    "HDR": hdr_effect,
    "Sharpen": sharpen,
    "Cool Tone": cool_tone,
    "Warm Tone": warm_tone,
    "Noir B&W": noir_bw,
    "Vivid": vivid,
    "Bokeh": blur_bokeh,
}


def apply_effect(img_bgr, effect_name):
    func = EFFECTS.get(effect_name)
    if func is None:
        return img_bgr
    return func(img_bgr)
