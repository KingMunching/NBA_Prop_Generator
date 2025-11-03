import React, { useEffect, useState } from 'react';
import {
  Dialog,
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogHeader,
  DialogTitle,
} from '@/components/ui/dialog';
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ChartContainer } from '@/components/ui/chart';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, ResponsiveContainer, Cell, ReferenceLine, Tooltip } from 'recharts';
import { Calendar, TrendingUp, Target, User, X } from 'lucide-react';
import api from '../api';

const CustomTooltip = ({ active, payload, label, propType }) => {
  if (active && payload && payload.length) {
    return (
      <div className="bg-slate-900/80 backdrop-blur-sm border border-slate-700 rounded-lg p-2 shadow-xl text-center">
        <p className="text-white font-bold text-lg">{payload[0].value} <span className="text-xs text-slate-400">{propType}</span></p>
        <p className="text-slate-400 text-xs">{label}</p>
      </div>
    );
  }

  return null;
};

const PropStatsDialog = ({ prop, isOpen, onClose }) => {
  const [stats, setStats] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [imageError, setImageError] = useState(false);

  useEffect(() => {
    if (isOpen && prop) {
      fetchPlayerStats();
    }
  }, [isOpen, prop]);

  const fetchPlayerStats = async () => {
    try {
      setLoading(true);
      setError(null);
      const numGames = prop.num_games || prop.games_analyzed || 10;
      console.log('Fetching stats for player:', prop.nba_id, 'num_games:', numGames);
      const response = await api.get(`/players/${prop.nba_id}/stats?num_games=${numGames}`);
      console.log('Stats response:', response.data);
      
      // Transform the stats data for the chart
      const transformedStats = response.data.map((stat) => {
        const statValue = getStatValue(stat, prop.prop_type);
        const isHit = prop.direction === 'Over' ? statValue > prop.stat : statValue < prop.stat;
        
        return {
          date: new Date(stat.date).toLocaleDateString('en-US', { month: '2-digit', day: '2-digit', year: 'numeric' }),
          value: statValue,
          isHit: isHit,
          threshold: prop.stat,
        };
      }).reverse(); // Reverse to show oldest to newest

      setStats(transformedStats);
    } catch (err) {
      console.error('Error fetching player stats:', err);
      setError('Failed to load player statistics');
    } finally {
      setLoading(false);
    }
  };

  const getStatValue = (stat, propType) => {
    const statMap = {
      'PTS': stat.pts,
      'AST': stat.ast,
      'REB': stat.reb,
      'STL': stat.stl,
      'BLK': stat.blk,
      '3PM': stat.three_pm,
    };
    return statMap[propType] || 0;
  };

  const getPropTypeLabel = (type) => {
    const labelMap = {
      'PTS': 'Points',
      'AST': 'Assists',
      'REB': 'Rebounds',
      'STL': 'Steals',
      'BLK': 'Blocks',
      '3PM': '3-Pointers Made'
    };
    return labelMap[type] || type;
  };

  const chartConfig = {
    value: {
      label: getPropTypeLabel(prop?.prop_type),
    },
  };

  const headshotUrl = prop?.headshot_url || 
    (prop?.nba_id ? `https://cdn.nba.com/headshots/nba/latest/260x190/${prop.nba_id}.png` : null);

  const hits = stats.filter(s => s.isHit).length;
  const misses = stats.length - hits;
  const hitRate = stats.length > 0 ? ((hits / stats.length) * 100).toFixed(1) : 0;

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent className="max-w-4xl max-h-[90vh] overflow-y-auto bg-slate-800 border-slate-700 p-0">
        <DialogClose asChild>
          <button className="absolute top-3 right-3 z-10 w-8 h-8 rounded-full bg-slate-700/50 hover:bg-slate-600/80 flex items-center justify-center transition-colors">
            <X className="h-4 w-4 text-slate-400" />
          </button>
        </DialogClose>
        <div className="p-6 pt-12">
        <DialogHeader>
          <DialogTitle className="flex items-center gap-3 text-white">
            <div className="bg-slate-700/50 rounded-lg p-2 border border-slate-600">
              {headshotUrl && !imageError ? (
                <img 
                  src={headshotUrl}
                  alt={prop?.player_name}
                  className="w-12 h-12 object-cover rounded"
                  onError={() => setImageError(true)}
                />
              ) : (
                <div className="w-12 h-12 flex items-center justify-center bg-slate-600/50 rounded">
                  <User className="w-8 h-8 text-slate-400" />
                </div>
              )}
            </div>
            <div>
              <div className="text-xl font-bold">{prop?.player_name}</div>
              <div className="text-sm text-slate-400 font-normal">
                {getPropTypeLabel(prop?.prop_type)} - {prop?.direction} {prop?.stat}
              </div>
            </div>
          </DialogTitle>
          <DialogDescription className="text-slate-400">
            Last {stats.length} games performance analysis
          </DialogDescription>
        </DialogHeader>

        {loading ? (
          <div className="flex items-center justify-center py-12">
            <div className="text-slate-400">Loading statistics...</div>
          </div>
        ) : error ? (
          <div className="flex items-center justify-center py-12">
            <div className="text-red-400">{error}</div>
          </div>
        ) : (
          <div className="space-y-6">
            {/* Summary Cards */}
            <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
              <Card className="bg-slate-700/50 border-slate-600">
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm text-slate-400">Success Rate</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className={`text-2xl font-bold ${
                    hitRate >= 80 ? 'text-green-400' : hitRate >= 60 ? 'text-yellow-400' : 'text-red-400'
                  }`}>
                    {hitRate}%
                  </div>
                </CardContent>
              </Card>

              <Card className="bg-slate-700/50 border-slate-600">
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm text-slate-400">Hits</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-green-400">{hits}</div>
                </CardContent>
              </Card>

              <Card className="bg-slate-700/50 border-slate-600">
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm text-slate-400">Misses</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-red-400">{misses}</div>
                </CardContent>
              </Card>

              <Card className="bg-slate-700/50 border-slate-600">
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm text-slate-400">Player Avg</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold text-blue-400">{prop?.player_avg}</div>
                </CardContent>
              </Card>
            </div>

            {/* Bar Chart */}
            <Card className="bg-slate-700/50 border-slate-600">
              <CardHeader>
                <CardTitle className="text-white flex items-center gap-2">
                  <BarChart className="h-5 w-5" />
                  Game-by-Game Performance
                </CardTitle>
                <div className="text-sm text-slate-400 mt-2 flex flex-wrap gap-4">
                  <span className="inline-flex items-center gap-2">
                    <span className="w-3 h-3 bg-green-500 rounded"></span>
                    Hit ({prop?.direction})
                  </span>
                  <span className="inline-flex items-center gap-2">
                    <span className="w-3 h-3 bg-red-500 rounded"></span>
                    Miss
                  </span>
                  <span className="inline-flex items-center gap-2">
                    <span className="w-8 h-0.5 bg-blue-500 border-t-2 border-dashed border-blue-500"></span>
                    Threshold ({prop?.stat})
                  </span>
                </div>
              </CardHeader>
              <CardContent>
                <ChartContainer config={chartConfig} className="h-[400px] w-full">
                  <ResponsiveContainer width="100%" height="100%">
                    <BarChart data={stats} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
                      <CartesianGrid strokeDasharray="3 3" stroke="#475569" />
                      <XAxis 
                        dataKey="date" 
                        stroke="#e2e8f0"
                        tick={{ fill: '#e2e8f0' }}
                        angle={-45}
                        textAnchor="end"
                        height={80}
                      />
                      <YAxis 
                        stroke="#e2e8f0"
                        tick={{ fill: '#e2e8f0' }}
                        domain={[0, 'dataMax + 5']}
                        tickFormatter={(value) => Math.floor(value)}
                      />
                      {/* Threshold line - MUST be before bars */}
                      <ReferenceLine 
                        y={prop?.stat} 
                        stroke="#3b82f6" 
                        strokeWidth={3}
                        strokeDasharray="8 4"
                        label={{ 
                          value: `${prop?.stat}`, 
                          fill: '#3b82f6', 
                          fontSize: 14,
                          fontWeight: 'bold',
                          position: 'right' 
                        }}
                      />
                      <Tooltip
                        cursor={false}
                        content={<CustomTooltip propType={prop?.prop_type} />}
                      />
                      <Bar dataKey="value" radius={[4, 4, 0, 0]}>
                        {stats.map((entry, index) => (
                          <Cell 
                            key={`cell-${index}`} 
                            fill={entry.isHit ? 'rgba(34, 197, 94, 0.7)' : 'rgba(239, 68, 68, 0.7)'} 
                          />
                        ))}
                      </Bar>
                    </BarChart>
                  </ResponsiveContainer>
                </ChartContainer>
              </CardContent>
            </Card>

            {/* Stats Table */}
            <Card className="bg-slate-700/50 border-slate-600">
              <CardHeader>
                <CardTitle className="text-white flex items-center gap-2">
                  <Calendar className="h-5 w-5" />
                  Detailed Stats
                </CardTitle>
              </CardHeader>
              <CardContent>
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="border-b border-slate-600">
                        <th className="text-left text-slate-400 py-2 px-4">Date</th>
                        <th className="text-left text-slate-400 py-2 px-4">{getPropTypeLabel(prop?.prop_type)}</th>
                        <th className="text-left text-slate-400 py-2 px-4">Threshold</th>
                        <th className="text-left text-slate-400 py-2 px-4">Result</th>
                      </tr>
                    </thead>
                    <tbody>
                      {stats.map((stat, index) => (
                        <tr key={index} className="border-b border-slate-700 hover:bg-slate-600/30">
                          <td className="py-2 px-4 text-slate-300">{stat.date}</td>
                          <td className="py-2 px-4 text-white font-medium">{stat.value}</td>
                          <td className="py-2 px-4 text-blue-400">{stat.threshold}</td>
                          <td className="py-2 px-4">
                            <span className={`px-2 py-1 rounded text-xs font-medium ${
                              stat.isHit 
                                ? 'bg-green-500/20 text-green-400' 
                                : 'bg-red-500/20 text-red-400'
                            }`}>
                              {stat.isHit ? 'HIT' : 'MISS'}
                            </span>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </CardContent>
            </Card>
          </div>
        )}
        </div>
      </DialogContent>
    </Dialog>
  );
};

export default PropStatsDialog;