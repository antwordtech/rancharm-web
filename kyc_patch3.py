with open('kyc.html') as f:
    c = f.read()
before = c

old_markup = '''      <label class="photo-upload-box" id="selfieBox">
        <i class="fa-solid fa-camera"></i>
        <div style="font-weight:700;font-size:13px;">Take a picture of yourself</div>
        <div style="font-size:11px;color:var(--text-dim);margin-top:4px;">Tap to open camera</div>
        <img id="selfiePreview" class="photo-preview" style="display:none;">
        <input type="file" accept="image/*" capture="user" id="selfieFile" style="display:none;" onchange="previewPhoto(this,'selfieBox','selfiePreview')">
      </label>
      <label class="photo-upload-box" id="idBox">
        <i class="fa-solid fa-id-card"></i>
        <div style="font-weight:700;font-size:13px;">Take a picture of your ID (front)</div>
        <div style="font-size:11px;color:var(--text-dim);margin-top:4px;">Tap to open camera</div>
        <img id="idPreview" class="photo-preview" style="display:none;">
        <input type="file" accept="image/*" capture="environment" id="idFile" style="display:none;" onchange="previewPhoto(this,'idBox','idPreview')">
      </label>'''

new_markup = '''      <label class="photo-upload-box" id="selfieBox">
        <div class="photo-icon-circle"><i class="fa-solid fa-camera"></i></div>
        <div class="photo-upload-title" id="selfieTitle">Take a picture of yourself</div>
        <div class="photo-upload-hint" id="selfieHint">Tap to open camera</div>
        <div class="photo-preview-wrap" id="selfiePreviewWrap" style="display:none;">
          <img id="selfiePreview" class="photo-preview">
          <div class="photo-check-badge"><i class="fa-solid fa-check"></i></div>
        </div>
        <input type="file" accept="image/*" capture="user" id="selfieFile" style="display:none;" onchange="previewPhoto(this,'selfieBox','selfiePreview','selfiePreviewWrap','selfieTitle','selfieHint')">
      </label>
      <label class="photo-upload-box" id="idBox">
        <div class="photo-icon-circle"><i class="fa-solid fa-id-card"></i></div>
        <div class="photo-upload-title" id="idTitle">Take a picture of your ID (front)</div>
        <div class="photo-upload-hint" id="idHint">Tap to open camera</div>
        <div class="photo-preview-wrap" id="idPreviewWrap" style="display:none;">
          <img id="idPreview" class="photo-preview">
          <div class="photo-check-badge"><i class="fa-solid fa-check"></i></div>
        </div>
        <input type="file" accept="image/*" capture="environment" id="idFile" style="display:none;" onchange="previewPhoto(this,'idBox','idPreview','idPreviewWrap','idTitle','idHint')">
      </label>'''

if old_markup not in c:
    print('MARKUP PATTERN NOT FOUND - check manually')
c = c.replace(old_markup, new_markup)

old_js = '''  window.previewPhoto = (input, boxId, previewId) => {
    const file = input.files[0];
    if (!file) return;
    const url = URL.createObjectURL(file);
    const preview = document.getElementById(previewId);
    preview.src = url;
    preview.style.display = 'block';
    document.getElementById(boxId).classList.add('has-file');
  };'''

new_js = '''  window.previewPhoto = (input, boxId, previewId, wrapId, titleId, hintId) => {
    const file = input.files[0];
    if (!file) return;
    const url = URL.createObjectURL(file);
    document.getElementById(previewId).src = url;
    document.getElementById(wrapId).style.display = 'block';
    document.getElementById(boxId).classList.add('has-file');
    document.getElementById(titleId).textContent = 'Photo captured';
    document.getElementById(hintId).textContent = 'Tap to retake';
  };'''

if old_js not in c:
    print('JS PATTERN NOT FOUND - check manually')
c = c.replace(old_js, new_js)

with open('kyc.html', 'w') as f:
    f.write(c)
print('OK' if c != before else 'NO CHANGE')
