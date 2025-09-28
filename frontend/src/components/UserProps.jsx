import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { BookmarkCheck, TrendingUp, Users, Target, Zap, RefreshCw, Trash2, Calendar, BarChart3 } from 'lucide-react';
import Navbar from './Navbar';
import PropCard from './PropCard';

import api from "../api"; 
import { supabase } from "../lib/supabase"; 

const UserProps = () => {
    const navigate = useNavigate();
    const [savedProps, setSavedProps] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    

    useEffect(() => {
        fetchSavedProps();
    }, []);

    const fetchSavedProps = async () => {
        try {
            setLoading(true);
            // Get JWT from Supabase
            const { data, error } = await supabase.auth.getSession();
            if (error || !data.session) {
                setError("You must be logged in to view saved props.");
                setLoading(false);
                return;
            }
            const token = data.session.access_token;
            
            const response = await api.get("/props/", {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            setSavedProps(response.data.props || []);
        } catch (err) {
            console.error("Error fetching saved props:", err);
            const message = err.response?.data?.detail || err.message || "Unknown error";
            setError("Error loading saved props: " + message);
        } finally {
            setLoading(false);
        }
    };

    const handleDelete = async (propId) => {
        if (!window.confirm("Are you sure you want to delete this saved prop?")) {
            return;
        }

        try {
            // Get JWT from Supabase
            const { data, error } = await supabase.auth.getSession();
            if (error || !data.session) {
                alert("You must be logged in to delete props.");
                return;
            }
            const token = data.session.access_token;
            
            await api.delete(`/props/delete/${propId}`, {
                headers: {
                    Authorization: `Bearer ${token}`,
                },
            });

            // Remove from local state
            setSavedProps(savedProps.filter(prop => prop.id !== propId));
            
        } catch (err) {
            console.error("Error deleting prop:", err);
            const message = err.response?.data?.detail || err.message || "Unknown error";
            alert("Error deleting prop: " + message);
        }
    };

    const getPropTypeIcon = (type) => {
        const iconMap = {
            'PTS': Target,
            'AST': Users,
            'REB': TrendingUp,
            'STL': Zap,
            'BLK': Target,
            '3PM': Target
        };
        return iconMap[type] || Target;
    };

    const getPropTypeLabel = (type) => {
        const labelMap = {
            'PTS': 'Points',
            'AST': 'Assists',
            'REB': 'Rebounds',
            'STL': 'Steals',
            'BLK': 'Blocks',
            '3PM': '3-Pointers'
        };
        return labelMap[type] || type;
    };

    const handleNewSearch = () => {
        navigate('/props/form');
    };

    const formatDate = (dateString) => {
        return new Date(dateString).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    };

    if (loading) {
        return (
            <div>
                <Navbar />
                <div className="min-h-screen bg-gradient-to-r from-slate-900 to-slate-700 p-4">
                    <div className="max-w-6xl mx-auto">
                        <div className="text-center py-16">
                            <div className="bg-slate-800 border-slate-700 rounded-lg p-8 shadow-xl max-w-md mx-auto">
                                <RefreshCw className="h-16 w-16 mx-auto mb-4 text-blue-400 animate-spin" />
                                <h3 className="text-white text-xl font-semibold mb-2">Loading Your Props</h3>
                                <p className="text-slate-400 text-sm">Please wait while we fetch your saved props...</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    if (error) {
        return (
            <div>
                <Navbar />
                <div className="min-h-screen bg-gradient-to-r from-slate-900 to-slate-700 p-4">
                    <div className="max-w-6xl mx-auto">
                        <div className="text-center py-16">
                            <div className="bg-slate-800 border-slate-700 rounded-lg p-8 shadow-xl max-w-md mx-auto">
                                <Target className="h-16 w-16 mx-auto mb-4 text-red-400 opacity-50" />
                                <h3 className="text-white text-xl font-semibold mb-2">Error Loading Props</h3>
                                <p className="text-slate-400 text-sm mb-4">{error}</p>
                                <Button
                                    onClick={() => window.location.reload()}
                                    className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white"
                                >
                                    Retry
                                </Button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div>
            <Navbar />
            <div className="min-h-screen bg-gradient-to-r from-slate-900 to-slate-700 p-4">
                <div className="max-w-6xl mx-auto">
                    {/* Header Section */}
                    <div className="mb-8">
                        <div className="flex items-center justify-between mb-4">
                            <div className="flex items-center space-x-2">
                                <BookmarkCheck className="h-8 w-8 text-blue-400" />
                                <h1 className="text-white text-3xl font-bold">My Saved Props</h1>
                            </div>
                            
                            <Button
                                onClick={handleNewSearch}
                                className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white"
                            >
                                <Target className="h-4 w-4 mr-2" />
                                Find New Props
                            </Button>
                        </div>
                        
                        <div className="bg-slate-800 border-slate-700 rounded-lg p-6 shadow-xl">
                            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 text-sm">
                                <div className="bg-slate-700/50 p-3 rounded-lg">
                                    <span className="text-slate-400">Total Saved Props:</span>
                                    <div className="text-white font-medium text-2xl">{savedProps.length}</div>
                                </div>
                                <div className="bg-slate-700/50 p-3 rounded-lg">
                                    <span className="text-slate-400">Average Success Rate:</span>
                                    <div className="text-white font-medium text-2xl">
                                        {savedProps.length > 0 ? 
                                            `${(savedProps.reduce((acc, prop) => acc + prop.threshold, 0) / savedProps.length * 100).toFixed(1)}%` : 
                                            '0%'
                                        }
                                    </div>
                                </div>
                                <div className="bg-slate-700/50 p-3 rounded-lg">
                                    <span className="text-slate-400">Last Updated:</span>
                                    <div className="text-white font-medium">
                                        {savedProps.length > 0 ? 
                                            formatDate(Math.max(...savedProps.map(p => new Date(p.created_at)))) : 
                                            'No props saved'
                                        }
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Results Section */}
                    {savedProps.length > 0 ? (
                        <div className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
                            {savedProps.map((prop, index) => (
                                    <PropCard 
                                        key={prop.id || index}
                                        prop={prop}
                                        onDelete={handleDelete}
                                        onViewDetails={(prop) => console.log('View details for:', prop)}
                                        isSaved={true}
                                    />
                                ))}
                        </div>
                    ) : (
                        <div className="text-center py-16">
                            <div className="bg-slate-800 border-slate-700 rounded-lg p-8 shadow-xl max-w-md mx-auto">
                                <div className="text-slate-400 mb-4">
                                    <BookmarkCheck className="h-16 w-16 mx-auto mb-4 opacity-50" />
                                </div>
                                <h3 className="text-white text-xl font-semibold mb-2">No Saved Props</h3>
                                <p className="text-slate-400 text-sm mb-4">
                                    You haven't saved any props yet. Start by searching for props and save the ones you like!
                                </p>
                                <Button
                                    onClick={handleNewSearch}
                                    className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white"
                                >
                                    <Target className="h-4 w-4 mr-2" />
                                    Find Props
                                </Button>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default UserProps;