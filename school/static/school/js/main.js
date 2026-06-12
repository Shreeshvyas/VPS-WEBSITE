document.addEventListener('DOMContentLoaded', () => {

    /* ==========================================================================
       1. THEME TOGGLE (LIGHT / DARK MODE)
       ========================================================================== */
    const themeToggleBtn = document.getElementById('theme-toggle');
    const themeIcon = themeToggleBtn.querySelector('i');
    
    // Check local storage or system preferences
    const savedTheme = localStorage.getItem('theme');
    const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
    
    const setDarkMode = (isDark) => {
        if (isDark) {
            document.documentElement.setAttribute('data-theme', 'dark');
            themeIcon.className = 'fa-solid fa-sun';
            localStorage.setItem('theme', 'dark');
        } else {
            document.documentElement.removeAttribute('data-theme');
            themeIcon.className = 'fa-solid fa-moon';
            localStorage.setItem('theme', 'light');
        }
    };

    // Initialize theme
    if (savedTheme === 'dark' || (!savedTheme && systemPrefersDark)) {
        setDarkMode(true);
    } else {
        setDarkMode(false);
    }

    // Toggle theme on button click
    themeToggleBtn.addEventListener('click', () => {
        const isCurrentlyDark = document.documentElement.getAttribute('data-theme') === 'dark';
        setDarkMode(!isCurrentlyDark);
        showToast('Theme switched successfully!', 'success');
    });


    /* ==========================================================================
       2. MOBILE NAVIGATION
       ========================================================================== */
    const mobileNavToggle = document.querySelector('.mobile-nav-toggle');
    const navMenu = document.querySelector('.nav-menu');
    
    if (mobileNavToggle && navMenu) {
        mobileNavToggle.addEventListener('click', () => {
            mobileNavToggle.classList.toggle('active');
            navMenu.classList.toggle('active');
        });
        
        // Close menu when clicking a link
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', () => {
                mobileNavToggle.classList.remove('active');
                navMenu.classList.remove('active');
            });
        });
    }


    /* ==========================================================================
       3. HERO SLIDER (HOMEPAGE CAROUSEL)
       ========================================================================== */
    const slides = document.querySelectorAll('.slide');
    const dotsContainer = document.querySelector('.slider-dots');
    const prevBtn = document.querySelector('.slider-arrow-left');
    const nextBtn = document.querySelector('.slider-arrow-right');
    
    if (slides.length > 0) {
        let currentSlide = 0;
        let slideInterval;
        const intervalTime = 6000; // 6 seconds

        // Create dots dynamically
        slides.forEach((_, idx) => {
            const dot = document.createElement('button');
            dot.classList.add('slider-dot');
            if (idx === 0) dot.classList.add('active');
            dot.setAttribute('aria-label', `Go to slide ${idx + 1}`);
            dotsContainer.appendChild(dot);
            
            dot.addEventListener('click', () => {
                goToSlide(idx);
                resetInterval();
            });
        });

        const dots = document.querySelectorAll('.slider-dot');

        const goToSlide = (n) => {
            slides[currentSlide].classList.remove('active');
            dots[currentSlide].classList.remove('active');
            currentSlide = (n + slides.length) % slides.length;
            slides[currentSlide].classList.add('active');
            dots[currentSlide].classList.add('active');
        };

        const nextSlide = () => {
            goToSlide(currentSlide + 1);
        };

        const prevSlide = () => {
            goToSlide(currentSlide - 1);
        };

        if (nextBtn) {
            nextBtn.addEventListener('click', () => {
                nextSlide();
                resetInterval();
            });
        }

        if (prevBtn) {
            prevBtn.addEventListener('click', () => {
                prevSlide();
                resetInterval();
            });
        }

        // Auto play function
        const startInterval = () => {
            slideInterval = setInterval(nextSlide, intervalTime);
        };

        const resetInterval = () => {
            clearInterval(slideInterval);
            startInterval();
        };

        // Initialize slider auto play
        startInterval();
    }


    /* ==========================================================================
       4. ANIMATED STATISTICS COUNTERS (Intersection Observer)
       ========================================================================== */
    const statsSection = document.querySelector('.stats-section');
    const statNumbers = document.querySelectorAll('.stat-number');
    
    if (statsSection && statNumbers.length > 0) {
        let animated = false;

        const animateCounters = () => {
            statNumbers.forEach(counter => {
                const target = parseInt(counter.getAttribute('data-target'), 10);
                const suffix = counter.getAttribute('data-suffix') || '';
                let count = 0;
                const speed = 2000 / target; // complete in 2 seconds
                
                const updateCount = () => {
                    const increment = Math.ceil(target / 40);
                    if (count < target) {
                        count += increment;
                        if (count > target) count = target;
                        counter.innerText = count + suffix;
                        setTimeout(updateCount, 40);
                    } else {
                        counter.innerText = target + suffix;
                    }
                };
                
                updateCount();
            });
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting && !animated) {
                    animateCounters();
                    animated = true;
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.2 });

        observer.observe(statsSection);
    }


    /* ==========================================================================
       5. GALLERY FILTERING
       ========================================================================== */
    const filterButtons = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item');
    
    if (filterButtons.length > 0 && galleryItems.length > 0) {
        filterButtons.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class from buttons
                filterButtons.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                
                const filterValue = btn.getAttribute('data-filter');
                
                galleryItems.forEach(item => {
                    // Fade out transition
                    item.style.transform = 'scale(0.8)';
                    item.style.opacity = '0';
                    
                    setTimeout(() => {
                        if (filterValue === 'all' || item.getAttribute('data-category') === filterValue) {
                            item.style.display = 'block';
                            setTimeout(() => {
                                item.style.transform = 'scale(1)';
                                item.style.opacity = '1';
                            }, 50);
                        } else {
                            item.style.display = 'none';
                        }
                    }, 300);
                });
            });
        });
    }


    /* ==========================================================================
       6. LIGHTBOX MODAL (Gallery Previews)
       ========================================================================== */
    const lightbox = document.createElement('div');
    lightbox.className = 'lightbox';
    document.body.appendChild(lightbox);
    
    lightbox.innerHTML = `
        <button class="lightbox-close" aria-label="Close Lightbox">&times;</button>
        <button class="lightbox-arrow lightbox-arrow-left" aria-label="Previous Image"><i class="fa-solid fa-chevron-left"></i></button>
        <div class="lightbox-content">
            <img class="lightbox-img" src="" alt="Zoomed view">
            <div class="lightbox-caption"></div>
        </div>
        <button class="lightbox-arrow lightbox-arrow-right" aria-label="Next Image"><i class="fa-solid fa-chevron-right"></i></button>
    `;

    const lightboxImg = lightbox.querySelector('.lightbox-img');
    const lightboxCaption = lightbox.querySelector('.lightbox-caption');
    const lightboxClose = lightbox.querySelector('.lightbox-close');
    const lBoxPrevBtn = lightbox.querySelector('.lightbox-arrow-left');
    const lBoxNextBtn = lightbox.querySelector('.lightbox-arrow-right');
    
    let activeImagesList = [];
    let currentImageIndex = 0;

    const openLightbox = (index) => {
        currentImageIndex = index;
        const imgObj = activeImagesList[currentImageIndex];
        
        lightboxImg.src = imgObj.src;
        lightboxCaption.innerText = imgObj.caption;
        
        lightbox.classList.add('active');
        document.body.style.overflow = 'hidden';
    };

    const closeLightbox = () => {
        lightbox.classList.remove('active');
        document.body.style.overflow = 'auto';
    };

    const navigateLightbox = (direction) => {
        currentImageIndex = (currentImageIndex + direction + activeImagesList.length) % activeImagesList.length;
        const imgObj = activeImagesList[currentImageIndex];
        
        lightboxImg.style.opacity = '0';
        setTimeout(() => {
            lightboxImg.src = imgObj.src;
            lightboxCaption.innerText = imgObj.caption;
            lightboxImg.style.opacity = '1';
        }, 150);
    };

    // Attach click events to gallery items
    if (galleryItems.length > 0) {
        galleryItems.forEach(item => {
            item.addEventListener('click', () => {
                // Populate active list of images matching current filter
                const activeFilter = document.querySelector('.filter-btn.active')?.getAttribute('data-filter') || 'all';
                activeImagesList = [];
                let itemIndex = 0;
                let clickedIndex = 0;
                
                galleryItems.forEach(gItem => {
                    const gCat = gItem.getAttribute('data-category');
                    if (activeFilter === 'all' || gCat === activeFilter) {
                        const img = gItem.querySelector('img');
                        const cap = gItem.querySelector('.gallery-overlay h4')?.innerText || '';
                        
                        activeImagesList.push({
                            src: img.src,
                            caption: cap
                        });
                        
                        if (gItem === item) {
                            clickedIndex = itemIndex;
                        }
                        itemIndex++;
                    }
                });
                
                openLightbox(clickedIndex);
            });
        });
    }

    if (lightboxClose) {
        lightboxClose.addEventListener('click', closeLightbox);
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) closeLightbox();
        });
        
        lBoxPrevBtn.addEventListener('click', () => navigateLightbox(-1));
        lBoxNextBtn.addEventListener('click', () => navigateLightbox(1));
        
        // Keyboard controls
        document.addEventListener('keydown', (e) => {
            if (!lightbox.classList.contains('active')) return;
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft') navigateLightbox(-1);
            if (e.key === 'ArrowRight') navigateLightbox(1);
        });
    }


    /* ==========================================================================
       7. CONTACT FORM SUBMISSION (AJAX / Fetch)
       ========================================================================== */
    const contactForm = document.getElementById('school-contact-form');
    
    if (contactForm) {
        contactForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const submitBtn = contactForm.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn.innerHTML;
            
            // Disable button and show spinner/loading text
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Sending...';
            
            const formData = new FormData(contactForm);
            const actionUrl = contactForm.getAttribute('action');
            
            fetch(actionUrl, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            })
            .then(async response => {
                const data = await response.json();
                if (!response.ok) {
                    throw new Error(data.message || 'Network response was not ok');
                }
                return data;
            })
            .then(data => {
                showToast(data.message, 'success');
                contactForm.reset();
            })
            .catch(error => {
                showToast(error.message || 'Something went wrong. Please try again.', 'error');
            })
            .finally(() => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnText;
            });
        });
    }


    /* ==========================================================================
       8. TOAST NOTIFICATION UTILITY
       ========================================================================== */
    const createToastContainer = () => {
        let container = document.querySelector('.toast-container');
        if (!container) {
            container = document.createElement('div');
            container.className = 'toast-container';
            document.body.appendChild(container);
        }
        return container;
    };

    const showToast = (message, type = 'success') => {
        const container = createToastContainer();
        const toast = document.createElement('div');
        toast.className = `toast toast-${type}`;
        
        const iconClass = type === 'success' ? 'fa-circle-check' : 'fa-circle-exclamation';
        
        toast.innerHTML = `
            <span class="toast-icon"><i class="fa-solid ${iconClass}"></i></span>
            <span class="toast-message">${message}</span>
        `;
        
        container.appendChild(toast);
        
        // Trigger reflow for slide animation
        toast.offsetHeight;
        toast.classList.add('show');
        
        // Remove toast after 4 seconds
        setTimeout(() => {
            toast.classList.remove('show');
            setTimeout(() => {
                toast.remove();
            }, 400);
        }, 4000);
    };

    /* ==========================================================================
       9. BACK TO TOP BUTTON
       ========================================================================== */
    const backToTopBtn = document.getElementById('back-to-top');
    if (backToTopBtn) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 400) {
                backToTopBtn.classList.add('show');
            } else {
                backToTopBtn.classList.remove('show');
            }
        });
        
        backToTopBtn.addEventListener('click', () => {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }


    /* ==========================================================================
       10. SCROLL REVEAL ANIMATION (Smooth entrance effects)
       ========================================================================== */
    const revealElements = document.querySelectorAll(
        '.facility-card, .teacher-card, .stat-card, .notice-card, .event-item-card, .gallery-item, .contact-info-card, .contact-form-panel, .curriculum-card'
    );
    
    revealElements.forEach(el => el.classList.add('scroll-reveal'));
    
    const revealObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('reveal-active');
                revealObserver.unobserve(entry.target);
            }
        });
    }, {
        threshold: 0.05,
        rootMargin: '0px 0px -40px 0px'
    });

    document.querySelectorAll('.scroll-reveal').forEach(el => {
        revealObserver.observe(el);
    });

});

// 11. PRELOADER FADEOUT (Runs after assets are fully loaded)
window.addEventListener('load', () => {
    const preloader = document.getElementById('preloader');
    if (preloader) {
        preloader.style.opacity = '0';
        preloader.style.visibility = 'hidden';
        setTimeout(() => {
            preloader.remove();
        }, 500);
    }
});
