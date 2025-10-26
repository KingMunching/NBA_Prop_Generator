import React, { useState } from 'react';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Target, Users, TrendingUp, Zap, Calendar, BarChart3, Trash2, PlusCircle, User } from 'lucide-react';

const PropCard = ({ prop, onSave, onDelete, onViewDetails, isSaved = false }) => {
    const [imageError, setImageError] = useState(false);
    
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

    const formatDate = (dateString) => {
        return new Date(dateString).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric',
            hour: '2-digit',
            minute: '2-digit'
        });
    };

    const Icon = getPropTypeIcon(prop.prop_type);
    const successRate =  prop.success_rate
    const gamesAnalyzed = isSaved ? prop.num_games : prop.games_analyzed;
    const headshotUrl = prop.headshot_url || (prop.nba_id ? `https://cdn.nba.com/headshots/nba/latest/260x190/${prop.nba_id}.png` : null);

    return (
        <Card className="bg-slate-800 border-slate-700 shadow-lg hover:shadow-xl transition-all duration-200 hover:scale-[1.02] w-full">
            <CardHeader className="pb-3">
                <div className="flex items-start justify-between gap-3">
                    <div className="flex-1 min-w-0">
                        <CardTitle className="text-white text-lg font-bold flex items-center gap-2 flex-wrap">
                            <span className="truncate">{prop.player_name}</span>
                            
                        </CardTitle>
                           <div className="mt-1.5 bg-gradient-to-r from-blue-500/10 to-purple-500/10 border border-blue-400/20 rounded-md px-3 py-1.5">
                            <p className="text-slate-300 text-sm">
                                {getPropTypeLabel(prop.prop_type)} <span className="font-bold text-white">{prop.direction} {prop.stat}</span>
                            </p>
                        </div>
                    </div>
                    <div className="bg-slate-700/50 rounded-lg p-2 border border-slate-600 flex-shrink-0">
                        {headshotUrl && !imageError ? (
                            <img 
                                src={headshotUrl}
                                alt={prop.player_name}
                                className="w-14 h-14 object-cover rounded"
                                onError={() => setImageError(true)}
                            />
                        ) : (
                            <div className="w-14 h-14 flex items-center justify-center bg-slate-600/50 rounded">
                                <User className="w-8 h-8 text-slate-400" />
                            </div>
                        )}
                    </div>
                </div>
            </CardHeader>
            <CardContent className="space-y-3">
                <div className="space-y-2">
                    <div className="flex items-center justify-between">
                        <span className="text-slate-300 text-sm">Success Rate:</span>
                        <span className={`font-bold text-base ${
                            successRate >= 0.9 ? 'text-green-400' : 
                            successRate >= 0.8 ? 'text-blue-400' : 
                            'text-yellow-400'
                        }`}>
                            {(successRate * 100).toFixed(1)}%
                        </span>
                    </div>
                    <div className="flex items-center justify-between">
                        <span className="text-slate-300 text-sm">Games Analyzed:</span>
                        <span className="text-blue-400 font-medium">
                            {gamesAnalyzed}
                        </span>
                    </div>
                    <div className="flex items-center justify-between">
                        <span className="text-slate-300 text-sm">Player Avg:</span>
                        <span className="text-blue-400 font-medium">
                            {prop.player_avg}
                        </span>
                    </div>
                    <div className="flex items-center justify-between">
                        <span className="text-slate-300 text-sm">Z-Score:</span>
                        <span className="text-blue-400 font-medium">
                            {prop.z_score}
                        </span>
                    </div>
                    
                </div>
                
                <div className="w-full bg-slate-700 rounded-full h-2 overflow-hidden">
                    <div 
                        className={`h-2 rounded-full transition-all duration-300 ${
                            successRate >= 0.9 ? 'bg-green-400' : 
                            successRate >= 0.8 ? 'bg-blue-400' : 
                            'bg-yellow-400'
                        }`}
                        style={{ width: `${Math.min(successRate * 100, 100)}%` }}
                    />
                </div>
                
                {isSaved && prop.created_at && (
                    <div className="flex items-center justify-between text-xs pt-1 border-t border-slate-700">
                        <span className="text-slate-400 flex items-center">
                            <Calendar className="h-3 w-3 mr-1" />
                            Saved:
                        </span>
                        <span className="text-slate-300">
                            {formatDate(prop.created_at)}
                        </span>
                    </div>
                )}
                
                <div className="flex gap-2 pt-1">
                    {!isSaved && onSave && (
                        <Button
                            onClick={() => onSave(prop)}
                            className="flex-1 bg-gradient-to-r from-green-600 to-green-700 hover:from-green-700 hover:to-green-800 text-white"
                            size="sm"
                        >
                            <PlusCircle className="h-4 w-4 mr-1.5" />
                            Save
                        </Button>
                    )}
                    <Button 
                        className="flex-1 bg-gradient-to-r from-blue-600 to-blue-700 hover:from-blue-700 hover:to-blue-800 text-white font-medium rounded-md transition-all duration-200"
                        size="sm"
                        onClick={() => onViewDetails(prop)}
                    >
                        <BarChart3 className="h-4 w-4 mr-1.5" />
                        Details
                    </Button>
                    {isSaved && onDelete && (
                        <Button 
                            variant="outline"
                            size="icon"
                            className="border-red-600/50 text-red-400 hover:bg-red-600/20 hover:text-red-300 hover:border-red-500 transition-all duration-200"
                            onClick={() => onDelete(prop.id)}
                        >
                            <Trash2 className="h-4 w-4" />
                        </Button>
                    )}
                </div>
            </CardContent>
        </Card>
    );
};

export default PropCard;