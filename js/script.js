document.addEventListener("DOMContentLoaded", () => {
    /* ==============================================
       THEME TOGGLE
       ============================================== */
    const themeBtns = document.querySelectorAll(".theme-toggle");
    
    // Check saved theme or system preference
    const currentTheme = localStorage.getItem("theme");
    if (currentTheme) {
        document.documentElement.setAttribute("data-theme", currentTheme);
    } else {
        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            document.documentElement.setAttribute("data-theme", "dark");
        }
    }

    themeBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            let theme = document.documentElement.getAttribute("data-theme");
            if (theme === "dark") {
                document.documentElement.removeAttribute("data-theme");
                localStorage.setItem("theme", "light");
            } else {
                document.documentElement.setAttribute("data-theme", "dark");
                localStorage.setItem("theme", "dark");
            }
        });
    });

    /* ==============================================
       DASHBOARD SIDEBAR (Rule 49)
       ============================================== */
    const toggleSidebar = document.getElementById("mobile-sidebar-toggle");
    const closeSidebar = document.getElementById("sidebar-close");
    const sidebar = document.getElementById("dashboard-sidebar");
    const sidebarOverlay = document.getElementById("sidebar-overlay");

    function closeAllSidebarItems() {
        if (sidebar) sidebar.classList.remove("active");
        if (sidebarOverlay) sidebarOverlay.classList.remove("active");
    }

    if (toggleSidebar && sidebar) {
        toggleSidebar.addEventListener("click", () => {
            sidebar.classList.toggle("active");
            if (sidebarOverlay) sidebarOverlay.classList.toggle("active");
        });
    }

    if (closeSidebar) {
        closeSidebar.addEventListener("click", closeAllSidebarItems);
    }

    if (sidebarOverlay) {
        sidebarOverlay.addEventListener("click", closeAllSidebarItems);
    }

    // Close on link click on mobile
    const sidebarLinks = document.querySelectorAll(".sidebar-link");
    sidebarLinks.forEach(link => {
        link.addEventListener("click", () => {
            if (window.innerWidth <= 992) {
                closeAllSidebarItems();
            }
        });
    });

    /* ==============================================
       RTL TOGGLE
       ============================================== */
    const rtlBtns = document.querySelectorAll(".rtl-toggle");
    const currentRtl = localStorage.getItem("rtl");

    if (currentRtl === "enabled") {
        document.documentElement.setAttribute("dir", "rtl");
    }

    rtlBtns.forEach(btn => {
        btn.addEventListener("click", () => {
            const isRtl = document.documentElement.getAttribute("dir") === "rtl";
            if (isRtl) {
                document.documentElement.removeAttribute("dir");
                localStorage.setItem("rtl", "disabled");
            } else {
                document.documentElement.setAttribute("dir", "rtl");
                localStorage.setItem("rtl", "enabled");
            }
        });
    });

    /* ==============================================
       BACK TO TOP
       ============================================== */
    const backToTopBtn = document.getElementById("back-to-top");

    if (backToTopBtn) {
        window.addEventListener("scroll", () => {
            if (window.pageYOffset > 300) {
                backToTopBtn.classList.add("active");
            } else {
                backToTopBtn.classList.remove("active");
            }
        });

        backToTopBtn.addEventListener("click", () => {
            window.scrollTo({
                top: 0,
                behavior: "smooth"
            });
        });
    }

    /* ==============================================
       MOBILE MENU (Rule 14 & 15)
       ============================================== */
    const hamburger = document.getElementById("hamburger");
    const mobileNav = document.getElementById("mobile-nav");
    const mobileOverlay = document.getElementById("mobile-overlay");

    function toggleMenu() {
        if (!mobileNav) return;
        const isActive = mobileNav.classList.contains("active");
        if (isActive) {
            mobileNav.classList.remove("active");
            mobileOverlay.classList.remove("active");
            document.body.style.overflow = "auto";
        } else {
            mobileNav.classList.add("active");
            mobileOverlay.classList.add("active");
            document.body.style.overflow = "hidden"; // Prevent background scrolling
        }
    }

    if (hamburger) hamburger.addEventListener("click", toggleMenu);
    if (mobileOverlay) mobileOverlay.addEventListener("click", toggleMenu);

    /* ==============================================
       ACTIVE LINK HIGHLIGHTING (Rule 12 & 33)
       ============================================== */
    const currentPath = window.location.pathname.split("/").pop();
    const navLinks = document.querySelectorAll(".nav-link");
    
    navLinks.forEach(link => {
        // Basic match by href text
        const href = link.getAttribute("href");
        if (href === currentPath || (currentPath === "" && href === "index.html")) {
            link.classList.add("active");
            
            // If it's in a dropdown, highlight the parent too
            const parentNavItem = link.closest(".nav-item.dropdown");
            if (parentNavItem) {
                parentNavItem.classList.add("active");
            } else {
                // For non-dropdown links, highlight the parent li if it's not a dropdown item
                const li = link.closest("li");
                if (li && !li.closest(".dropdown-menu")) {
                    li.classList.add("active");
                }
            }
        }
    });

    const filterBtn = document.getElementById("filter-btn");
    const filterDropdown = document.getElementById("filter-dropdown");
    if (filterBtn && filterDropdown) {
        filterBtn.addEventListener("click", (e) => {
            e.stopPropagation();
            filterDropdown.classList.toggle("active");
        });
        document.addEventListener("click", (e) => {
            if (filterDropdown && !filterDropdown.contains(e.target)) {
                filterDropdown.classList.remove("active");
            }
        });
    }

    /* ==============================================
       FAQ ACCORDION
       ============================================== */
    const faqQuestions = document.querySelectorAll(".faq-question");
    
    faqQuestions.forEach(question => {
        question.addEventListener("click", () => {
            const item = question.parentElement;
            const isActive = item.classList.contains("active");
            
            // Close all other items (accordion behavior)
            document.querySelectorAll(".faq-item").forEach(otherItem => {
                otherItem.classList.remove("active");
            });
            
            // Toggle current item
            if (!isActive) {
                item.classList.add("active");
            }
        });
    });

    // Password Visibility Toggle
    const togglePasswordIcons = document.querySelectorAll('.toggle-password');
    togglePasswordIcons.forEach(icon => {
        icon.addEventListener('click', function() {
            const wrapper = this.parentElement;
            const passwordInput = wrapper.querySelector('input');
            
            // Toggle the type attribute
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            
            // Toggle the icon
            this.classList.toggle('fa-eye');
            this.classList.toggle('fa-eye-slash');
        });
    });
});
