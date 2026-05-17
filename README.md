# 🎓 kating.AI

> Transform casual text into polished academic language with AI-powered intelligence.

[![Live Demo](https://img.shields.io/badge/demo-live-brightgreen?style=flat-square)](https://kating-ai.vercel.app)
[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](LICENSE)
[![Language](https://img.shields.io/badge/language-TypeScript-3178c6?style=flat-square)](https://www.typescriptlang.org/)

## 📋 Overview

**kating.AI** is a web application designed to help students, academics, and professionals convert informal or casual text into formal academic language. Whether you're working on a thesis, journal article, or academic assignment, kating.AI makes it easy to elevate your writing to a professional standard.

### Key Features

- ✨ **AI-Powered Humanization** - Convert raw text to natural academic language
- 📊 **Real-time Word Counter** - Track word count with a 300-word free tier limit
- 📋 **Copy to Clipboard** - Easily copy converted text for further use
- 🎨 **Modern UI/UX** - Beautiful, responsive design built with shadcn/ui
- 🚀 **Fast Processing** - Quick text transformation powered by a dedicated backend
- 🆓 **Free Tier** - Start using without creating an account
- 💳 **Premium Tier** - Upgrade for unlimited text conversion (coming soon)

## 🛠️ Tech Stack

### Frontend
- **Framework**: [React](https://react.dev/) 18.3.1
- **Language**: [TypeScript](https://www.typescriptlang.org/) 5.8.3
- **Build Tool**: [Vite](https://vitejs.dev/) 5.4.19
- **Styling**: [Tailwind CSS](https://tailwindcss.com/) 3.4.17
- **UI Components**: [shadcn/ui](https://ui.shadcn.com/)
- **State Management**: [TanStack React Query](https://tanstack.com/query/latest) 5.83.0
- **Form Handling**: [React Hook Form](https://react-hook-form.com/) 7.61.1
- **Validation**: [Zod](https://zod.dev/) 3.25.76
- **Routing**: [React Router](https://reactrouter.com/) 6.30.1
- **Icons**: [Lucide React](https://lucide.dev/) 0.462.0

### Backend
- **Runtime**: Python
- **Deployment**: Render
- **API Endpoint**: `https://kating-ai-backend.onrender.com/api/humanize`

### Language Composition
- TypeScript: 92.6%
- Python: 3.3%
- CSS: 2.8%
- Other: 1.3%

## 🚀 Getting Started

### Prerequisites
- Node.js 16+ (install via [nvm](https://github.com/nvm-sh/nvm#installing-and-updating))
- npm or yarn

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/reynaldaryansyah25/kating.AI.git
cd kating.AI
```

2. **Navigate to frontend directory**
```bash
cd frontend
```

3. **Install dependencies**
```bash
npm install
```

4. **Start the development server**
```bash
npm run dev
```

The application will be available at `http://localhost:8080`

### Build for Production

```bash
npm run build
```

Output files will be generated in the `dist/` directory.

## 📦 Available Scripts

In the `frontend` directory, you can run:

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server with hot reload |
| `npm run build` | Build for production |
| `npm run build:dev` | Build for development mode |
| `npm run lint` | Run ESLint code quality checks |
| `npm run preview` | Preview production build locally |

## 📁 Project Structure

```
kating.AI/
├── frontend/                  # React application
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   ├── pages/            # Page components (Index, NotFound)
│   │   ├── hooks/            # Custom React hooks
│   │   ├── lib/              # Utility functions
│   │   ├── App.tsx           # Root component
│   │   └── main.tsx          # Entry point
│   ├── public/               # Static assets
│   ├── vite.config.ts        # Vite configuration
│   ├── tailwind.config.ts    # Tailwind CSS configuration
│   ├── tsconfig.json         # TypeScript configuration
│   ├── eslint.config.js      # ESLint configuration
│   └── package.json          # Dependencies and scripts
└── README.md                 # This file
```

## 🎯 How It Works

1. **Input Text**: Users paste or type their informal text into the input textarea
2. **Word Validation**: The application checks if the text exceeds the 300-word limit for the free tier
3. **API Processing**: Text is sent to the kating.AI backend API for humanization
4. **Output Display**: The converted academic text is displayed in the output textarea
5. **Copy & Use**: Users can easily copy the result and use it in their documents

### Free Tier Limitations
- Maximum 300 words per request
- No account required
- Community-driven support

### Premium Features (Coming Soon)
- Unlimited word count
- Batch processing
- Priority processing
- Advanced analytics
- Custom tone preferences

## 🔗 API Integration

The frontend communicates with the backend API:

```
POST https://kating-ai-backend.onrender.com/api/humanize
```

**Request Body:**
```json
{
  "text": "your text here"
}
```

**Response:**
```json
{
  "result": "humanized academic text"
}
```

**Error Handling:**
- Empty text validation
- Word count verification
- Network error handling with user-friendly messages
- Toast notifications for user feedback

## 🎨 Design System

The application uses a custom Tailwind CSS theme with:
- **Typography**: Source Serif 4 for headings, Plus Jakarta Sans for body
- **Colors**: HSL-based color system for flexibility
- **Components**: Built with Radix UI primitives for accessibility
- **Animations**: Smooth transitions and accordion animations
- **Responsive**: Mobile-first approach with breakpoints for all device sizes

## 🌐 Deployment

### Frontend Deployment
The application is deployed on **Vercel**: https://kating-ai.vercel.app

**Deployment Steps:**
1. Push changes to the `main` branch
2. Vercel automatically builds and deploys
3. Preview and production environments available

### Custom Domain
To connect a custom domain:
1. Navigate to Project > Settings > Domains
2. Click "Connect Domain"
3. Follow the domain configuration instructions

## 🔒 Security & Privacy

- No user data is stored locally
- No account creation required for free tier
- SSL/TLS encryption for API communication
- Input sanitization and validation
- CORS configuration for trusted domains

## 📊 Performance

- Optimized bundle size with tree-shaking
- Code splitting for faster initial load
- Image optimization
- Lazy loading of components
- Efficient state management with React Query

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Code Quality

- **Linting**: ESLint with modern rules
- **Type Safety**: Full TypeScript coverage
- **Code Formatting**: Consistent with project standards
- **Testing**: Ready for unit and integration tests

## 🐛 Known Issues & Roadmap

### Current Phase
- [x] Basic text humanization
- [x] Word count tracking
- [x] Copy to clipboard
- [ ] Premium tier implementation
- [ ] Batch processing
- [ ] Multiple language support
- [ ] Mobile app version
- [ ] Advanced customization options

## 📞 Support & Contact

- **Live Demo**: [kating-ai.vercel.app](https://kating-ai.vercel.app)
- **Issues**: [GitHub Issues](https://github.com/reynaldaryansyah25/kating.AI/issues)
- **Author**: [@reynaldaryansyah25](https://github.com/reynaldaryansyah25)

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- [shadcn/ui](https://ui.shadcn.com/) - Beautiful component library
- [Radix UI](https://www.radix-ui.com/) - Unstyled, accessible components
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first CSS framework
- [Vercel](https://vercel.com/) - Deployment platform
- [Render](https://render.com/) - Backend hosting

---

<div align="center">

**[⬆ back to top](#-katingai)**

Made with ❤️ by [Reynald Ary Ansyah](https://github.com/reynaldaryansyah25)

</div>
