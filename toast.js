(function(){
  if(!document.getElementById('fintech-toast-style')){
    const s=document.createElement('style');
    s.id='fintech-toast-style';
    s.textContent=`
    #toast{position:fixed;top:-80px;left:50%;transform:translateX(-50%);min-width:280px;max-width:90%;background:#fff;border-radius:14px;box-shadow:0 12px 32px rgba(15,23,42,.16);padding:14px 18px;display:flex;align-items:center;gap:12px;z-index:9999;transition:top .35s cubic-bezier(.4,0,.2,1);border-left:4px solid #14b8a6;font-family:Inter,system-ui,-apple-system,sans-serif}
    #toast.show{top:20px}
    #toast.success{border-left-color:#10b981}
    #toast.error{border-left-color:#f43f5e}
    #toast .ti{font-size:18px;color:#14b8a6}
    #toast.success .ti{color:#10b981}
    #toast.error .ti{color:#f43f5e}
    #toast .tm{font-size:14px;font-weight:500;color:#334155}`;
    (document.head||document.documentElement).appendChild(s);
  }
  function ensureEl(){
    let t=document.getElementById('toast');
    if(!t){
      t=document.createElement('div');t.id='toast';
      t.innerHTML='<i class="ti fa-solid fa-circle-info"></i><span class="tm"></span>';
      (document.body||document.documentElement).appendChild(t);
    }
    return t;
  }
  if(document.body)ensureEl(); else document.addEventListener('DOMContentLoaded',ensureEl);
  let timer;
  window.toast=function(msg,type){
    const t=ensureEl();
    t.className='';if(type)t.classList.add(type);
    t.querySelector('.tm').textContent=msg;
    const ic=t.querySelector('.ti');
    ic.className='ti fa-solid '+(type==='success'?'fa-circle-check':type==='error'?'fa-circle-exclamation':'fa-circle-info');
    requestAnimationFrame(()=>t.classList.add('show'));
    clearTimeout(timer);timer=setTimeout(()=>t.classList.remove('show'),3200);
  };
})();
