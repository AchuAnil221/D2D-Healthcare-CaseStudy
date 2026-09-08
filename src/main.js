// Wait for DOM
document.addEventListener('DOMContentLoaded', () => {
  gsap.registerPlugin(ScrollTrigger);

  // 1. Hero Parallax
  gsap.to('.hero-mockup', {
    y: -100,
    rotateX: 0,
    ease: 'none',
    scrollTrigger: {
      trigger: '.hero',
      start: 'top top',
      end: 'bottom top',
      scrub: true
    }
  });

  // 2. Context Fade Lines
  const fadeLines = gsap.utils.toArray('.fade-line');
  fadeLines.forEach(line => {
    gsap.to(line, {
      opacity: 1,
      y: 0,
      duration: 1,
      ease: 'power2.out',
      scrollTrigger: {
        trigger: line,
        start: 'top 80%',
      }
    });
  });

  // 3. Vision Scale
  gsap.from('.vision-text', {
    scale: 0.9,
    opacity: 0,
    duration: 1.5,
    ease: 'power3.out',
    scrollTrigger: {
      trigger: '.vision',
      start: 'top 70%',
    }
  });

  // 4. System Breakdown Parallax
  const cards = gsap.utils.toArray('.card');
  cards.forEach(card => {
    const speed = card.getAttribute('data-speed');
    gsap.to(card, {
      y: () => -50 * speed,
      ease: 'none',
      scrollTrigger: {
        trigger: '.breakdown',
        start: 'top bottom',
        end: 'bottom top',
        scrub: true
      }
    });
  });

  // 5. Product Experience (Pinned Scrubbing)
  const screens = gsap.utils.toArray('.screen');
  const labels = gsap.utils.toArray('.label');
  
  if (screens.length > 0) {
    const tl = gsap.timeline({
      scrollTrigger: {
        trigger: '.product-experience',
        start: 'top top',
        end: '+=200%',
        scrub: 1,
        pin: true,
      }
    });

    // Animate from screen 1 to 2
    tl.to('.s1', { opacity: 0, duration: 1 })
      .to('.s2', { opacity: 1, duration: 1 }, '<')
      .to('.label-track', { y: -40, duration: 1 }, '<')
      .to('.l1', { opacity: 0.5, duration: 0.1 }, '<')
      .to('.l2', { opacity: 1, duration: 0.1 }, '<')
      
      // Animate from screen 2 to 3
      .to('.s2', { opacity: 0, duration: 1 })
      .to('.s3', { opacity: 1, duration: 1 }, '<')
      .to('.label-track', { y: -80, duration: 1 }, '<')
      .to('.l2', { opacity: 0.5, duration: 0.1 }, '<')
      .to('.l3', { opacity: 1, duration: 0.1 }, '<');
  }

  // 7. Technology Diagram Slide In
  gsap.from('.tech-img', {
    x: -50,
    opacity: 0,
    duration: 1,
    ease: 'power2.out',
    scrollTrigger: {
      trigger: '.technology',
      start: 'top 60%',
    }
  });

  gsap.from('.tech-list li', {
    x: 50,
    opacity: 0,
    duration: 0.8,
    stagger: 0.2,
    ease: 'power2.out',
    scrollTrigger: {
      trigger: '.technology',
      start: 'top 60%',
    }
  });

  // 8. Impact Numbers Scale up
  gsap.from('.number', {
    scale: 0.5,
    opacity: 0,
    duration: 1,
    stagger: 0.2,
    ease: 'back.out(1.7)',
    scrollTrigger: {
      trigger: '.impact',
      start: 'top 70%',
    }
  });

  // 9. Final Showcase Layered Parallax Zoom Out
  gsap.to('.showcase-collage', {
    scale: 0.8,
    ease: 'none',
    scrollTrigger: {
      trigger: '.showcase',
      start: 'top bottom',
      end: 'bottom top',
      scrub: true
    }
  });

  gsap.to('.img1', { y: -100, ease: 'none', scrollTrigger: { trigger: '.showcase', scrub: true } });
  gsap.to('.img2', { y: 50, ease: 'none', scrollTrigger: { trigger: '.showcase', scrub: true } });
  gsap.to('.img3', { y: -50, ease: 'none', scrollTrigger: { trigger: '.showcase', scrub: true } });

});
