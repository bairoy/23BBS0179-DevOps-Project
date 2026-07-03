/**
 * ABC Technologies - Interactive JavaScript Controller
 */

document.addEventListener('DOMContentLoaded', () => {
  // Active link highlighting
  const currentPath = window.location.pathname.split('/').pop() || 'index.html';
  const navLinks = document.querySelectorAll('.nav-links a');
  
  navLinks.forEach(link => {
    const linkHref = link.getAttribute('href');
    if (linkHref === currentPath || (currentPath === '' && linkHref === 'index.html')) {
      link.classList.add('active');
    }
  });

  // Animated number counters for statistics
  const counters = document.querySelectorAll('.counter-val');
  if (counters.length > 0) {
    const speed = 150;
    counters.forEach(counter => {
      const updateCount = () => {
        const target = +counter.getAttribute('data-target');
        const count = +counter.innerText;
        const inc = Math.max(1, Math.ceil(target / speed));

        if (count < target) {
          counter.innerText = count + inc;
          setTimeout(updateCount, 20);
        } else {
          counter.innerText = target;
        }
      };
      updateCount();
    });
  }

  // Handle Form Submissions with visual feedback
  const forms = document.querySelectorAll('form');
  forms.forEach(form => {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const submitBtn = form.querySelector('button[type="submit"]');
      if (submitBtn) {
        const originalText = submitBtn.innerText;
        submitBtn.innerText = 'Transmitting Data...';
        submitBtn.disabled = true;

        setTimeout(() => {
          submitBtn.innerText = '✓ Successfully Received!';
          submitBtn.style.background = '#10b981';
          form.reset();
          setTimeout(() => {
            submitBtn.innerText = originalText;
            submitBtn.style.background = '';
            submitBtn.disabled = false;
          }, 3500);
        }, 1200);
      }
    });
  });
});
