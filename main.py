from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="theme-color" content="#667eea">
    <meta name="description" content="Avakin Life Shop - Premium Bot Subscriptions">
    <title>Avakin Life Shop | avakinlife.shop</title>
    
    <!-- Favicon -->
    <link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cdefs%3E%3ClinearGradient id='gold' x1='0%25' y1='0%25' x2='0%25' y2='100%25'%3E%3Cstop offset='0%25' style='stop-color:%23FFD700'/%3E%3Cstop offset='100%25' style='stop-color:%23B8860B'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='100' height='100' fill='%23000'/%3E%3Cpath d='M50 15 L60 25 L50 30 L40 25 Z' fill='url(%23gold)'/%3E%3Cpath d='M25 35 C25 35 20 40 25 70 C25 70 35 90 50 90 C65 90 75 70 75 70 C80 40 75 35 75 35 L25 35 Z' fill='url(%23gold)'/%3E%3Cpath d='M35 50 L40 45 L45 50 L40 48 Z M55 50 L60 45 L65 50 L60 48 Z' fill='%23000'/%3E%3Cpath d='M42 60 L50 65 L58 60 L50 62 Z' fill='%23000'/%3E%3Cpath d='M45 70 L50 75 L55 70' stroke='%23000' stroke-width='2' fill='none'/%3E%3C/svg%3E">
    <link rel="apple-touch-icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Cdefs%3E%3ClinearGradient id='gold' x1='0%25' y1='0%25' x2='0%25' y2='100%25'%3E%3Cstop offset='0%25' style='stop-color:%23FFD700'/%3E%3Cstop offset='100%25' style='stop-color:%23B8860B'/%3E%3C/linearGradient%3E%3C/defs%3E%3Crect width='100' height='100' fill='%23000'/%3E%3Cpath d='M50 15 L60 25 L50 30 L40 25 Z' fill='url(%23gold)'/%3E%3Cpath d='M25 35 C25 35 20 40 25 70 C25 70 35 90 50 90 C65 90 75 70 75 70 C80 40 75 35 75 35 L25 35 Z' fill='url(%23gold)'/%3E%3Cpath d='M35 50 L40 45 L45 50 L40 48 Z M55 50 L60 45 L65 50 L60 48 Z' fill='%23000'/%3E%3Cpath d='M42 60 L50 65 L58 60 L50 62 Z' fill='%23000'/%3E%3Cpath d='M45 70 L50 75 L55 70' stroke='%23000' stroke-width='2' fill='none'/%3E%3C/svg%3E">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        * {
            -webkit-tap-highlight-color: transparent;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.8; }
        }
        
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(20px); }
            to { opacity: 1; transform: translateY(0); }
        }
        
        @keyframes shine {
            0% { background-position: -200% center; }
            100% { background-position: 200% center; }
        }
        
        .animate-bounce {
            animation: bounce 2s infinite;
        }
        
        .animate-pulse {
            animation: pulse 2s infinite;
        }
        
        .fade-in {
            animation: fadeIn 0.6s ease-out;
        }
        
        .gradient-bg {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
            min-height: 100vh;
        }
        
        .premium-shine {
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
            background-size: 200% 100%;
            animation: shine 3s infinite;
        }
        
        button, a {
            -webkit-touch-callout: none;
            touch-action: manipulation;
        }
        
        html {
            scroll-behavior: smooth;
        }
        
        @media (hover: none) {
            .hover-card:active {
                transform: scale(0.98);
            }
        }
    </style>
</head>
<body class="gradient-bg">
    <!-- Language Selector -->
    <div class="fixed top-2 right-2 sm:top-4 sm:right-4 flex flex-col sm:flex-row gap-2 z-50">
        <button onclick="changeLanguage('ar')" id="btn-ar" 
                class="px-3 py-2 sm:px-4 sm:py-2 rounded-lg bg-white text-purple-900 font-bold transition-all hover:scale-105 active:scale-95 text-sm sm:text-base shadow-lg">
            العربية
        </button>
        <button onclick="changeLanguage('en')" id="btn-en" 
                class="px-3 py-2 sm:px-4 sm:py-2 rounded-lg bg-purple-800 text-white font-bold transition-all hover:scale-105 active:scale-95 text-sm sm:text-base shadow-lg">
            EN
        </button>
        <button onclick="changeLanguage('pt')" id="btn-pt" 
                class="px-3 py-2 sm:px-4 sm:py-2 rounded-lg bg-purple-800 text-white font-bold transition-all hover:scale-105 active:scale-95 text-sm sm:text-base shadow-lg">
            PT
        </button>
    </div>

    <div class="container mx-auto px-3 sm:px-4 py-8 sm:py-12 pt-20 sm:pt-12">
        <!-- Header -->
        <div class="text-center mb-8 sm:mb-12 fade-in">
            <!-- Logo and Site Name -->
            <div class="flex items-center justify-center gap-3 mb-4">
                <div class="w-12 h-12 sm:w-16 sm:h-16">
                    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100" class="w-full h-full">
                        <defs>
                            <linearGradient id="gold" x1="0%" y1="0%" x2="0%" y2="100%">
                                <stop offset="0%" style="stop-color:#FFD700"/>
                                <stop offset="100%" style="stop-color:#B8860B"/>
                            </linearGradient>
                        </defs>
                        <rect width="100" height="100" fill="#000" rx="15"/>
                        <path d="M50 15 L60 25 L50 30 L40 25 Z" fill="url(#gold)"/>
                        <path d="M25 35 C25 35 20 40 25 70 C25 70 35 90 50 90 C65 90 75 70 75 70 C80 40 75 35 75 35 L25 35 Z" fill="url(#gold)"/>
                        <path d="M35 50 L40 45 L45 50 L40 48 Z M55 50 L60 45 L65 50 L60 48 Z" fill="#000"/>
                        <path d="M42 60 L50 65 L58 60 L50 62 Z" fill="#000"/>
                        <path d="M45 70 L50 75 L55 70" stroke="#000" stroke-width="2" fill="none"/>
                    </svg>
                </div>
                <div class="text-left">
                    <h2 class="text-xl sm:text-3xl font-bold text-yellow-400">avakinlife.shop</h2>
                    <p class="text-xs sm:text-sm text-purple-300">Premium Bot Store</p>
                </div>
            </div>
            
            <h1 id="main-title" class="text-3xl sm:text-5xl md:text-6xl font-bold text-white mb-3 sm:mb-4 animate-pulse leading-tight px-2">
                اشتراكات البوت المميز
            </h1>
            <p id="subtitle" class="text-base sm:text-xl md:text-2xl text-purple-200 px-4">
                اختر الباقة المناسبة لك
            </p>
        </div>

        <!-- Discord Button with Notice -->
        <div class="flex flex-col items-center mb-8 sm:mb-12 px-2 fade-in max-w-2xl mx-auto">
            <a href="https://discord.gg/rtaUJswERv" 
               target="_blank"
               rel="noopener noreferrer"
               class="group relative inline-flex items-center justify-center gap-2 sm:gap-4 bg-gradient-to-r from-indigo-600 to-purple-600 text-white px-6 py-4 sm:px-12 sm:py-6 rounded-xl sm:rounded-2xl text-lg sm:text-2xl md:text-3xl font-bold shadow-2xl hover:shadow-purple-500/50 transition-all duration-300 hover:scale-105 active:scale-95 animate-bounce w-full max-w-md">
                <svg class="w-6 h-6 sm:w-10 sm:h-10 group-hover:rotate-12 transition-transform flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"></path>
                </svg>
                <span id="discord-btn" class="text-center">انضم إلى سيرفر الديسكورد</span>
            </a>
            
            <!-- Notice about tutorial video -->
            <div class="mt-4 flex items-center gap-2 bg-white/20 backdrop-blur-md px-4 py-3 rounded-xl border border-purple-300 shadow-lg animate-pulse">
                <svg class="w-5 h-5 sm:w-6 sm:h-6 text-yellow-300 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                    <path d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z"></path>
                </svg>
                <p id="video-notice" class="text-white text-sm sm:text-base font-semibold text-center">
                    👇 شاهد فيديو الشرح أسفل الصفحة
                </p>
            </div>
        </div>

        <!-- Pricing Plans -->
        <div class="grid sm:grid-cols-2 gap-4 sm:gap-8 mb-8 sm:mb-12 max-w-5xl mx-auto" id="plans-container">
            <!-- Plans will be inserted here -->
        </div>

        <!-- YouTube Tutorial -->
        <div class="max-w-5xl mx-auto fade-in">
            <h2 id="tutorial-title" class="text-2xl sm:text-4xl font-bold text-white text-center mb-4 sm:mb-8">
                📺 شاهد فيديو الشرح
            </h2>
            <div class="bg-white/10 backdrop-blur-lg rounded-2xl sm:rounded-3xl p-3 sm:p-6 border-2 border-purple-400 shadow-2xl">
                <div class="relative pb-[56.25%] h-0 overflow-hidden rounded-xl sm:rounded-2xl bg-black">
                    <iframe
                        class="absolute top-0 left-0 w-full h-full"
                        src="https://www.youtube.com/embed/dQw4w9WgXcQ"
                        title="شرح استخدام البوت"
                        frameborder="0"
                        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen>
                    </iframe>
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="text-center mt-8 sm:mt-12 text-purple-200 px-4">
            <svg class="w-6 h-6 inline-block mb-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <p class="text-xs sm:text-sm" id="footer-text">يتم تحديد اللغة تلقائياً بناءً على موقعك 🌍</p>
        </div>
    </div>

    <script>
        const translations = {
            ar: {
                title: 'اشتراكات البوت المميز',
                subtitle: 'اختر الباقة المناسبة لك',
                discordBtn: 'انضم إلى سيرفر الديسكورد',
                videoNotice: '👇 شاهد فيديو الشرح أسفل الصفحة',
                tutorialTitle: '📺 شاهد فيديو الشرح',
                footer: 'يتم تحديد اللغة تلقائياً بناءً على موقعك 🌍',
                monthly: 'شهرياً',
                free: 'مجاني',
                direction: 'rtl',
                plans: [
                    {
                        name: 'الباقة المجانية',
                        nameEn: 'Free Plan',
                        price: '0',
                        oldPrice: null,
                        currency: 'مجاناً',
                        icon: '🎁',
                        features: [
                            '📊 نقاط يومية: 100',
                            '✏️ تغيير الاسم',
                            '🖼️ تغيير صورة الملف الشخصي',
                            '👥 عرض قائمة الأصدقاء',
                            '🚫 عرض قائمة المحظورين'
                        ],
                        popular: false,
                        buttonText: 'ابدأ مجاناً',
                        buttonColor: 'from-gray-600 to-gray-700',
                        limitedOffer: null
                    },
                    {
                        name: 'الباقة البريميوم',
                        nameEn: 'Premium Plan',
                        price: '15',
                        oldPrice: '18',
                        currency: '$',
                        icon: '👑',
                        features: [
                            '💎 نقاط يومية: 10,000',
                            '⭐ جميع مميزات الباقة المجانية',
                            '🎨 تصميمات حصرية',
                            '🚀 سرعة فائقة',
                            '💬 دعم أولوية VIP',
                            '🎯 مميزات إضافية'
                        ],
                        popular: true,
                        buttonText: 'احصل على البريميوم',
                        buttonColor: 'from-yellow-500 to-orange-500',
                        limitedOffer: 'عرض لفترة محدودة! 🔥'
                    }
                ]
            },
            en: {
                title: 'Premium Bot Subscriptions',
                subtitle: 'Choose the perfect plan for you',
                discordBtn: 'Join Discord Server',
                videoNotice: '👇 Watch tutorial video below',
                tutorialTitle: '📺 Watch Tutorial Video',
                footer: 'Language is automatically detected based on your location 🌍',
                monthly: '/month',
                free: 'Free',
                direction: 'ltr',
                plans: [
                    {
                        name: 'Free Plan',
                        nameEn: 'Free Plan',
                        price: '0',
                        oldPrice: null,
                        currency: 'Free',
                        icon: '🎁',
                        features: [
                            '📊 Daily Points: 100',
                            '✏️ Change Name',
                            '🖼️ Change Profile Picture',
                            '👥 View Friends List',
                            '🚫 View Blocked List'
                        ],
                        popular: false,
                        buttonText: 'Start Free',
                        buttonColor: 'from-gray-600 to-gray-700',
                        limitedOffer: null
                    },
                    {
                        name: 'Premium Plan',
                        nameEn: 'Premium Plan',
                        price: '15',
                        oldPrice: '18',
                        currency: '$',
                        icon: '👑',
                        features: [
                            '💎 Daily Points: 10,000',
                            '⭐ All Free Plan Features',
                            '🎨 Exclusive Designs',
                            '🚀 Ultra Speed',
                            '💬 VIP Priority Support',
                            '🎯 Extra Features'
                        ],
                        popular: true,
                        buttonText: 'Get Premium',
                        buttonColor: 'from-yellow-500 to-orange-500',
                        limitedOffer: 'Limited Time Offer! 🔥'
                    }
                ]
            },
            pt: {
                title: 'Assinaturas Premium do Bot',
                subtitle: 'Escolha o plano perfeito para você',
                discordBtn: 'Entrar no Servidor Discord',
                videoNotice: '👇 Assista ao vídeo tutorial abaixo',
                tutorialTitle: '📺 Assistir Vídeo Tutorial',
                footer: 'O idioma é detectado automaticamente com base na sua localização 🌍',
                monthly: '/mês',
                free: 'Grátis',
                direction: 'ltr',
                plans: [
                    {
                        name: 'Plano Gratuito',
                        nameEn: 'Free Plan',
                        price: '0',
                        oldPrice: null,
                        currency: 'Grátis',
                        icon: '🎁',
                        features: [
                            '📊 Pontos Diários: 100',
                            '✏️ Mudar Nome',
                            '🖼️ Mudar Foto de Perfil',
                            '👥 Ver Lista de Amigos',
                            '🚫 Ver Lista de Bloqueados'
                        ],
                        popular: false,
                        buttonText: 'Começar Grátis',
                        buttonColor: 'from-gray-600 to-gray-700',
                        limitedOffer: null
                    },
                    {
                        name: 'Plano Premium',
                        nameEn: 'Premium Plan',
                        price: '15',
                        oldPrice: '18',
                        currency: '$',
                        icon: '👑',
                        features: [
                            '💎 Pontos Diários: 10,000',
                            '⭐ Todos os Recursos Gratuitos',
                            '🎨 Designs Exclusivos',
                            '🚀 Velocidade Ultra',
                            '💬 Suporte VIP Prioritário',
                            '🎯 Recursos Extras'
                        ],
                        popular: true,
                        buttonText: 'Obter Premium',
                        buttonColor: 'from-yellow-500 to-orange-500',
                        limitedOffer: 'Oferta por Tempo Limitado! 🔥'
                    }
                ]
            }
        };

        let currentLanguage = 'ar';

        function detectLanguage() {
            fetch('https://ipapi.co/json/')
                .then(response => response.json())
                .then(data => {
                    const arabicCountries = ['SA', 'AE', 'EG', 'JO', 'LB', 'IQ', 'SY', 'YE', 'KW', 'QA', 'BH', 'OM', 'PS', 'DZ', 'MA', 'TN', 'LY', 'SD', 'MR'];
                    const portugueseCountries = ['BR', 'PT', 'AO', 'MZ'];
                    
                    if (arabicCountries.includes(data.country_code)) {
                        changeLanguage('ar');
                    } else if (portugueseCountries.includes(data.country_code)) {
                        changeLanguage('pt');
                    } else {
                        changeLanguage('en');
                    }
                })
                .catch(() => {
                    const userLang = navigator.language || navigator.userLanguage;
                    if (userLang.startsWith('ar')) {
                        changeLanguage('ar');
                    } else if (userLang.startsWith('pt')) {
                        changeLanguage('pt');
                    } else {
                        changeLanguage('en');
                    }
                });
        }

        function changeLanguage(lang) {
            currentLanguage = lang;
            const t = translations[lang];
            
            document.documentElement.dir = t.direction;
            document.getElementById('main-title').textContent = t.title;
            document.getElementById('subtitle').textContent = t.subtitle;
            document.getElementById('discord-btn').textContent = t.discordBtn;
            document.getElementById('video-notice').textContent = t.videoNotice;
            document.getElementById('tutorial-title').textContent = t.tutorialTitle;
            document.getElementById('footer-text').textContent = t.footer;
            
            updateButtonStyles(lang);
            renderPlans(t);
        }

        function updateButtonStyles(lang) {
            ['ar', 'en', 'pt'].forEach(l => {
                const btn = document.getElementById(`btn-${l}`);
                if (l === lang) {
                    btn.className = 'px-3 py-2 sm:px-4 sm:py-2 rounded-lg bg-white text-purple-900 font-bold transition-all hover:scale-105 active:scale-95 text-sm sm:text-base shadow-lg';
                } else {
                    btn.className = 'px-3 py-2 sm:px-4 sm:py-2 rounded-lg bg-purple-800 text-white font-bold transition-all hover:scale-105 active:scale-95 text-sm sm:text-base shadow-lg';
                }
            });
        }

        function renderPlans(t) {
            const container = document.getElementById('plans-container');
            container.innerHTML = '';
            
            t.plans.forEach((plan, index) => {
                const isPopular = plan.popular;
                const isFree = plan.price === '0';
                
                const planDiv = document.createElement('div');
                planDiv.className = `relative bg-white/10 backdrop-blur-lg rounded-2xl sm:rounded-3xl p-4 sm:p-8 border-2 transition-all duration-300 hover:scale-105 hover:shadow-2xl active:scale-95 fade-in ${
                    isPopular ? 'border-yellow-400 shadow-2xl shadow-yellow-400/30' : 'border-purple-400'
                }`;
                
                planDiv.style.animationDelay = `${index * 0.2}s`;
                
                const priceDisplay = isFree ? plan.currency : `${plan.currency}${plan.price}`;
                
                planDiv.innerHTML = `
                    ${isPopular ? `
                        <div class="absolute -top-4 left-1/2 transform -translate-x-1/2 bg-gradient-to-r from-yellow-400 to-orange-500 text-white font-bold px-4 sm:px-6 py-1 sm:py-2 rounded-full text-xs sm:text-sm shadow-lg premium-shine">
                            ⭐ ${currentLanguage === 'ar' ? 'الأكثر شعبية' : currentLanguage === 'pt' ? 'MAIS POPULAR' : 'MOST POPULAR'} ⭐
                        </div>
                    ` : ''}
                    
                    <div class="text-center mb-4 sm:mb-6">
                        <div class="text-4xl sm:text-6xl mb-3 sm:mb-4">${plan.icon}</div>
                        <h3 class="text-xl sm:text-3xl font-bold text-white mb-2 sm:mb-4">${plan.name}</h3>
                        
                        ${!isFree && plan.oldPrice ? `
                            <div class="mb-2">
                                <span class="text-xl sm:text-2xl text-red-400 line-through font-semibold">${plan.currency}${plan.oldPrice}</span>
                            </div>
                        ` : ''}
                        
                        <div class="text-3xl sm:text-5xl font-bold ${isFree ? 'text-green-400' : 'text-yellow-400'} mb-1 sm:mb-2">
                            ${priceDisplay}
                        </div>
                        
                        ${!isFree ? `
                            <p class="text-purple-300 text-sm sm:text-base mb-2">${t.monthly}</p>
                            ${plan.limitedOffer ? `
                                <div class="inline-block bg-red-500 text-white text-xs sm:text-sm font-bold px-3 py-1 rounded-full animate-pulse">
                                    ${plan.limitedOffer}
                                </div>
                            ` : ''}
                        ` : ''}
                    </div>
                    
                    <ul class="space-y-2 sm:space-y-3 mb-4 sm:mb-6">
                        ${plan.features.map(feature => `
                            <li class="flex items-start gap-2 sm:gap-3 text-purple-100 text-sm sm:text-lg">
                                <span>${feature}</span>
                            </li>
                        `).join('')}
                    </ul>
                    
                    <button onclick="window.open('https://discord.gg/rtaUJswERv', '_blank')"
                            class="w-full bg-gradient-to-r ${plan.buttonColor} text-white font-bold py-3 sm:py-4 px-4 sm:px-6 rounded-xl sm:rounded-2xl transition-all duration-300 hover:scale-105 active:scale-95 shadow-lg text-sm sm:text-lg">
                        ${plan.buttonText}
                    </button>
                `;
                
                container.appendChild(planDiv);
            });
        }

        detectLanguage();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"""
╔══════════════════════════════════════════╗
║   🚀 السيرفر يشتغل الآن!                ║
║                                          ║
║   🌐 افتح المتصفح على:                  ║
║   http://localhost:{port}                    ║
║   أو                                     ║
║   http://127.0.0.1:{port}                    ║
║                                          ║
║   💰 السعر: $15 بدل $18                 ║
║   📱 محسّن للجوال وسطح المكتب           ║
║   ⚡ اضغط Ctrl+C للإيقاف                ║
╚══════════════════════════════════════════╝
    """)
    app.run(host='0.0.0.0', port=9090, debug=True)