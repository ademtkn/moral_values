// Introduction kısmının animasyonu için
window.addEventListener('scroll', function() {
    const introSection = document.querySelector('.introduction');
    const introPosition = introSection.getBoundingClientRect().top;
    const screenPosition = window.innerHeight / 1.5;

    if (introPosition < screenPosition) {
        introSection.classList.add('visible');
    }
});

window.addEventListener('scroll', function() {
    var supportSection = document.querySelector('.support-us');
    var sectionPosition = supportSection.getBoundingClientRect().top;
    var screenPosition = window.innerHeight;

    if (sectionPosition < screenPosition) {
        supportSection.classList.add('visible');
    }
});

document.addEventListener("DOMContentLoaded", function() {
    const supportSection = document.querySelector(".support-us");
    window.addEventListener("scroll", function() {
        const sectionTop = supportSection.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        if (sectionTop < windowHeight - 100) {
            supportSection.classList.add("show");
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const fadeInSections = document.querySelectorAll(".fade-in-section");

    const observer = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add("show");
                observer.unobserve(entry.target); // Animasyon tamamlandıktan sonra gözlemlemeyi bırakır
            }
        });
    }, {
        threshold: 0.1 // Elemanın %10'u görünür olduğunda animasyon tetiklenir
    });

    fadeInSections.forEach(section => {
        observer.observe(section);
    });
});

document.addEventListener("DOMContentLoaded", function() {
    const teamMembers = document.querySelectorAll(".team-member");

    teamMembers.forEach((member, index) => {
        setTimeout(() => {
            member.classList.add("visible");
        }, index * 300); // Her üye için 300ms gecikme
    });
});

window.onscroll = function() {
    var header = document.querySelector("header");
    if (window.pageYOffset > 50) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
};

document.addEventListener('DOMContentLoaded', function() {
    const counters = document.querySelectorAll('.count');
    const speed = 200; // Sayacın hızını belirleyin

    counters.forEach(counter => {
        const animate = () => {
            const target = +counter.getAttribute('data-target');
            const count = +counter.innerText;

            // Artış miktarı her adımda 10
            const increment = 10;

            if (count < target) {
                counter.innerText = Math.min(count + increment, target);
                setTimeout(animate, 20); // 20 milisaniyede bir güncelleme
            } else {
                counter.innerText = target; // Hedefe ulaştığında durur
            }
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animate();
                    observer.unobserve(counter); // Sayaç bir kez çalıştıktan sonra gözlemciyi durdurur
                }
            });
        }, {
            threshold: 0.5 // Yüzde 50 göründüğünde animasyon başlar
        });

        observer.observe(counter);
    });
});

window.onscroll = function() {
    var header = document.querySelector("header");
    if (window.pageYOffset > 50) {
        header.classList.add("scrolled");
    } else {
        header.classList.remove("scrolled");
    }
};


