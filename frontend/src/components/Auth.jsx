import React, { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card'
import { Button } from '@/components/ui/button'
import { User, Mail, Lock, Eye, EyeOff } from 'lucide-react'
import { supabase } from '../lib/supabase'

const Auth = () => {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [isRegister, setIsRegister] = useState(false)
  const [showPassword, setShowPassword] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const navigate = useNavigate()

  const handleSubmit = async (e) => {
    e.preventDefault()
    setIsLoading(true)
    
    try {
      if (isRegister) {
        const { error } = await supabase.auth.signUp({ email, password })
        if (error) alert('Sign up error: ' + error.message)
        else alert('Check your email to confirm your account!')
      } else {
        const { error } = await supabase.auth.signInWithPassword({ email, password })
        if (error) {
          alert('Login error: ' + error.message)
        } else {
          navigate('/home') // Redirect to main app content
        }
      }
    } finally {
      setIsLoading(false)
    }
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-slate-900 to-slate-700 p-4">
      <div className="w-full max-w-md">
        {/* Logo Section */}
        <div className="text-center mb-8">
          <div className="flex items-center justify-center space-x-2 mb-4">
            <img 
              src="/proplogo.png" 
              alt="PropBets AI Logo" 
              className="h-12 w-12 object-contain"
            />
            <span className="text-white text-3xl font-bold">Hoop Intel</span>
          </div>
          <p className="text-slate-300 text-sm">
            Your stat-powered NBA betting companion
          </p>
        </div>

        {/* Auth Card */}
        <Card className="bg-slate-800 border-slate-700 shadow-2xl">
          <CardHeader className="pb-6">
            <CardTitle className="text-center text-white text-2xl font-bold">
              {isRegister ? 'Create Account' : 'Welcome Back'}
            </CardTitle>
            <p className="text-center text-slate-400 text-sm mt-2">
              {isRegister 
                ? 'Join thousands of smart bettors' 
                : 'Sign in to access your picks'
              }
            </p>
          </CardHeader>
          <CardContent className="space-y-6">
            <form onSubmit={handleSubmit} className="space-y-4">
              {/* Email Input */}
              <div className="relative">
                <Mail className="absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400 h-5 w-5" />
                <input
                  type="email"
                  placeholder="Email address"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  className="w-full pl-10 pr-4 py-3 bg-slate-700 border border-slate-600 rounded-md text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                />
              </div>

              {/* Password Input */}
              <div className="relative">
                <Lock className="absolute left-3 top-1/2 transform -translate-y-1/2 text-slate-400 h-5 w-5" />
                <input
                  type={showPassword ? "text" : "password"}
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  className="w-full pl-10 pr-12 py-3 bg-slate-700 border border-slate-600 rounded-md text-white placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute right-3 top-1/2 transform -translate-y-1/2 text-slate-400 hover:text-white transition-colors"
                >
                  {showPassword ? <EyeOff className="h-5 w-5" /> : <Eye className="h-5 w-5" />}
                </button>
              </div>

              {/* Submit Button */}
              <Button
                type="submit"
                disabled={isLoading}
                className="w-full bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-semibold py-3 rounded-md transition-all duration-200 transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none"
              >
                {isLoading ? (
                  <div className="flex items-center justify-center space-x-2">
                    <div className="w-4 h-4 border-2 border-white border-t-transparent rounded-full animate-spin"></div>
                    <span>{isRegister ? 'Creating Account...' : 'Signing In...'}</span>
                  </div>
                ) : (
                  <div className="flex items-center justify-center space-x-2">
                    <User className="h-5 w-5" />
                    <span>{isRegister ? 'Create Account' : 'Sign In'}</span>
                  </div>
                )}
              </Button>
            </form>

            {/* Divider */}
            <div className="relative">
              <div className="absolute inset-0 flex items-center">
                <div className="w-full border-t border-slate-600"></div>
              </div>
              <div className="relative flex justify-center text-sm">
                <span className="px-2 bg-slate-800 text-slate-400">or</span>
              </div>
            </div>

            {/* Toggle Auth Mode */}
            <div className="text-center">
              <button
                onClick={() => setIsRegister(!isRegister)}
                className="text-blue-400 hover:text-blue-300 transition-colors font-medium"
              >
                {isRegister 
                  ? 'Already have an account? Sign in' 
                  : 'Need an account? Create one'
                }
              </button>
            </div>

            {/* Additional Info */}
            <div className="text-center text-xs text-slate-500">
              {isRegister ? (
                <p>
                  By creating an account, you agree to our{' '}
                  <a href="#" className="text-blue-400 hover:text-blue-300">Terms of Service</a>
                  {' '}and{' '}
                  <a href="#" className="text-blue-400 hover:text-blue-300">Privacy Policy</a>
                </p>
              ) : (
                <p>
                  Forgot your password?{' '}
                  <a href="#" className="text-blue-400 hover:text-blue-300">Reset it here</a>
                </p>
              )}
            </div>
          </CardContent>
        </Card>

        {/* Footer */}
        <div className="text-center mt-8 text-slate-400 text-sm">
          <p>© 2025 Hoop Intel. All rights reserved.</p>
        </div>
      </div>
    </div>
  )
}

export default Auth