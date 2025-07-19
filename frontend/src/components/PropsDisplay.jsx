import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { ArrowLeft, TrendingUp, Users, Target, Zap, RefreshCw, ArrowUp, ArrowDown } from 'lucide-react';
import Navbar from './Navbar';

const PropDisplay = () => {
    const location = useLocation();
    const navigate = useNavigate();
    const [props, setProps] = useState([]);
    const [searchCriteria, setSearchCriteria] = useState({});

    useEffect(() => {
        // Get data from navigation state
        if (location.state) {
            setProps(location.state.props || []);
            setSearchCriteria(location.state.searchCriteria || {});
        } else {
            // If no state (direct navigation), redirect to form
            navigate('/props');
        }
    }, [location.state, navigate]);

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

    const getBetTypeIcon = (betType) => {
        return betType === 'over' ? ArrowUp : ArrowDown;
    };

    const getBetTypeColor = (betType) => {
        return betType === 'over' ? 'text-green-400' : 'text-red-400';
    };

    const getBetTypeBgColor = (betType) => {
        return betType === 'over' ? 'bg-green-500/20 border-green-500' : 'bg-red-500/20 border-red-500';
    };

    const handleBackToForm = () => {
        navigate('/props');
    };

    const handleNewSearch = () => {
        navigate('/props');
    };

    const Icon = getPropTypeIcon(searchCriteria.propType);

    // Group props by bet type for summary
    const overProps = props.filter(prop => prop.bet_type === 'over');
    const underProps = props.filter(prop => prop.bet_type === 'under');

    return (
        <div>
            <Navbar />
            <div className="min-h-screen bg-gradient-to-r from-slate-900 to-slate-700 p-4">
                <div className="max-w-6xl mx-auto">
                    {/* Header Section */}
                    <div className="mb-8">
                        <div className="flex items-center justify-between mb-4">
                            <Button
                                onClick={handleBackToForm}
                                variant="outline"
                                className="border-slate-600 bg-slate-700 text-slate-300 hover:bg-slate-600 hover:text-white"
                            >
                                <ArrowLeft className="h-4 w-4 mr-2" />
                                Back to Form
                            </Button>
                            
                            <Button
                                onClick={handleNewSearch}
                                className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white"
                            >
                                <RefreshCw className="h-4 w-4 mr-2" />
                                New Search
                            </Button>
                        </div>
                        
                        <div className="bg-slate-800 border-slate-700 rounded-lg p-6 shadow-xl">
                            <div className="flex items-center space-x-3 mb-4">
                                <Icon className="h-8 w-8 text-blue-400" />
                                <h1 className="text-white text-3xl font-bold">
                                    {getPropTypeLabel(searchCriteria.propType)} Props
                                </h1>
                            </div>
                            
                            <div className="grid grid-cols-2 md:grid-cols-6 gap-4 text-sm">
                                <div className="bg-slate-700/50 p-3 rounded-lg">
                                    <span className="text-slate-400">Min Success Rate:</span>
                                    <div className="text-white font-medium">{searchCriteria.minThreshold}%</div>
                                </div>
                                <div className="bg-slate-700/50 p-3 rounded-lg">
                                    <span className="text-slate-400">Games Analyzed:</span>
                                    <div className="text-white font-medium">{searchCriteria.numGames}</div>
                                </div>
                                <div className="bg-slate-700/50 p-3 rounded-lg">
                                    <span className="text-slate-400">Stat Line:</span>
                                    <div className="text-white font-medium">{searchCriteria.stat}</div>
                                </div>
                                <div className="bg-slate-700/50 p-3 rounded-lg">
                                    <span className="text-slate-400">Total Props:</span>
                                    <div className="text-white font-medium">{props.length}</div>
                                </div>
                                <div className="bg-green-500/20 p-3 rounded-lg border border-green-500">
                                    <span className="text-green-400">Overs:</span>
                                    <div className="text-white font-medium">{overProps.length}</div>
                                </div>
                                <div className="bg-red-500/20 p-3 rounded-lg border border-red-500">
                                    <span className="text-red-400">Unders:</span>
                                    <div className="text-white font-medium">{underProps.length}</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    {/* Results Section */}
                    {props.length > 0 ? (
                        <div className="grid gap-6 sm:grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
                            {props.map((prop, index) => {
                                const BetIcon = getBetTypeIcon(prop.bet_type);
                                return (
                                    <Card key={`${prop.player_id}-${prop.bet_type}` || index} className="bg-slate-800 border-slate-700 shadow-lg hover:shadow-xl transition-all duration-200 hover:scale-105">
                                        <CardHeader className="pb-3">
                                            <CardTitle className="text-white text-xl font-bold flex items-center justify-between">
                                                <span>{prop.player_name}</span>
                                                <Icon className="h-5 w-5 text-blue-400" />
                                            </CardTitle>
                                            <div className="flex items-center justify-between">
                                                <p className="text-slate-400 text-sm">
                                                    {getPropTypeLabel(prop.prop_type.toUpperCase())} {prop.stat}
                                                </p>
                                                <div className={`flex items-center space-x-1 px-3 py-1 rounded-full border ${getBetTypeBgColor(prop.bet_type)}`}>
                                                    <BetIcon className={`h-4 w-4 ${getBetTypeColor(prop.bet_type)}`} />
                                                    <span className={`text-sm font-bold uppercase ${getBetTypeColor(prop.bet_type)}`}>
                                                        {prop.bet_type}
                                                    </span>
                                                </div>
                                            </div>
                                        </CardHeader>
                                        <CardContent className="space-y-3">
                                            <div className="flex items-center justify-between">
                                                <span className="text-slate-300 text-sm">Success Rate:</span>
                                                <span className={`font-bold text-lg ${
                                                    prop.success_rate >= 0.9 ? 'text-green-400' : 
                                                    prop.success_rate >= 0.8 ? 'text-blue-400' : 
                                                    'text-yellow-400'
                                                }`}>
                                                    {(prop.success_rate * 100).toFixed(1)}%
                                                </span>
                                            </div>
                                            <div className="flex items-center justify-between">
                                                <span className="text-slate-300 text-sm">Games Analyzed:</span>
                                                <span className="text-blue-400 font-medium">
                                                    {prop.games_analyzed}
                                                </span>
                                            </div>
                                            
                                            {/* Success Rate Visual Bar */}
                                            <div className="space-y-2">
                                                <div className="w-full bg-slate-700 rounded-full h-2">
                                                    <div 
                                                        className={`h-2 rounded-full transition-all duration-300 ${
                                                            prop.success_rate >= 0.9 ? 'bg-green-400' : 
                                                            prop.success_rate >= 0.8 ? 'bg-blue-400' : 
                                                            'bg-yellow-400'
                                                        }`}
                                                        style={{ width: `${prop.success_rate * 100}%` }}
                                                    />
                                                </div>
                                            </div>
                                            
                                            {/* Prop Description */}
                                            <div className="bg-slate-700/50 p-3 rounded-lg text-center">
                                                <p className="text-slate-300 text-sm">
                                                    {prop.bet_type === 'over' ? 
                                                        `Player hits ${prop.stat}+ ${getPropTypeLabel(prop.prop_type.toUpperCase()).toLowerCase()}` :
                                                        `Player stays under ${prop.stat} ${getPropTypeLabel(prop.prop_type.toUpperCase()).toLowerCase()}`
                                                    }
                                                </p>
                                                <p className="text-slate-400 text-xs mt-1">
                                                    {Math.round(prop.success_rate * prop.games_analyzed)} out of {prop.games_analyzed} games
                                                </p>
                                            </div>
                                            
                                            {/* Action Button */}
                                            <Button 
                                                className={`w-full mt-4 font-medium py-2 rounded-md transition-all duration-200 ${
                                                    prop.bet_type === 'over' 
                                                        ? 'bg-gradient-to-r from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 text-white'
                                                        : 'bg-gradient-to-r from-red-600 to-red-700 hover:from-red-700 hover:to-red-800 text-white'
                                                }`}
                                                size="sm"
                                                onClick={() => {
                                                    console.log('View details for:', prop.player_name, prop.bet_type);
                                                }}
                                            >
                                                <BetIcon className="h-4 w-4 mr-2" />
                                                View {prop.bet_type.toUpperCase()} Details
                                            </Button>
                                        </CardContent>
                                    </Card>
                                );
                            })}
                        </div>
                    ) : (
                        <div className="text-center py-16">
                            <div className="bg-slate-800 border-slate-700 rounded-lg p-8 shadow-xl max-w-md mx-auto">
                                <div className="text-slate-400 mb-4">
                                    <Target className="h-16 w-16 mx-auto mb-4 opacity-50" />
                                </div>
                                <h3 className="text-white text-xl font-semibold mb-2">No Props Found</h3>
                                <p className="text-slate-400 text-sm mb-4">
                                    No props meet your selected criteria. Try adjusting your filters and search again.
                                </p>
                                <Button
                                    onClick={handleNewSearch}
                                    className="bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white"
                                >
                                    Adjust Filters
                                </Button>
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default PropDisplay;