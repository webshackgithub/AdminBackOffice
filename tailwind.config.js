/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './templates/**/*.html',
        './apps/**/*.html',
        './**/forms.py',
    ],
    theme: {
        extend: {
            colors: {
                brand: {
                    800: '#1E40AF',
                    900: '#1E3A8A',
                },
                slate: {
                    800: '#1E293B',
                    900: '#0F172A',
                },
                teal: {
                    500: '#14B8A6',
                },
                orange: {
                    500: '#F97316',
                }
            },
            fontFamily: {
                sans: ['Inter', 'ui-sans-serif', 'system-ui'],
            }
        },
    },
    plugins: [],
    darkMode: 'class',
}
