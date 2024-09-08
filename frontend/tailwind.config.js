module.exports = {
  content: [
    "./App.{js,jsx,ts,tsx}",
    "./app/**/*.{js,jsx,ts,tsx}",
    "./components/**/*.{js,jsx,ts,tsx}",
    "./app/(tabs)/meditate.tsx",
  ],
  theme: {
    extend: {},
    // Override the default fontFamily to avoid issues with missing fonts
    fontFamily: {
      sans: ['system-ui'], // Use system fonts
      serif: ['system-ui'], // Use system fonts for serif as well
    },
  },
  plugins: [],
};
