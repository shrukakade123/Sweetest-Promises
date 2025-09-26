function toggleMenu(){const nav=document.getElementById('mainnav');nav.classList.toggle('active')}
function openLightbox(img,caption){const lb=document.getElementById('lightbox');document.getElementById('lb-img').src=img.src;document.getElementById('lb-caption').innerText=caption;lb.style.display='flex'}
function closeLightbox(e){if(e.target.id==='lightbox'){document.getElementById('lightbox').style.display='none'}}
// simple confetti effect (shows brief confetti when called)
function showConfetti(){const c=document.getElementById('confetti');c.style.display='block';setTimeout(()=>c.style.display='none',1500)}
// auto show confetti if booking success message present
window.addEventListener('DOMContentLoaded',()=>{if(document.querySelector('.msg.success')){showConfetti()}})
