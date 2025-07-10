import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import api from "../api";
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { TrendingUp, Users, Target, AlertCircle, Zap } from 'lucide-react';
import Navbar from './Navbar';

const PropBetForm = () => {
    const navigate = useNavigate();
    const [propType, setPropType] = useState("PTS");
    const [numPlayers, setNumPlayers] = useState('3');
    const [minThreshold, setMinThreshold] = useState('80');
    const [error, setError] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [numGames, setNumGames] = useState('10');
    const [stat, setStat] = useState('10'); // Changed default to '10' to match PTS
    const [lines, setLines] = useState([])

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError('');
        setIsLoading(true);

        const payload = {
            prop_type: propType.toLowerCase(),
            stat: parseInt(stat),
            threshold: parseFloat(minThreshold) / 100,
            num_games: parseInt(numGames),
            num_rec: parseInt(numPlayers)
        };

        try {
            const response = await api.post('/props/today', payload);
            if (response.data.error) {
                setError(`Error: ${response.data.error}`);
            } else {
                // Navigate to results page with data and search criteria
                navigate('/props/results', {
                    state: {
                        props: response.data,
                        searchCriteria: {
                            propType,
                            numPlayers,
                            minThreshold,
                            numGames,
                            stat
                        }
                    }
                });
            }
        } catch (err) {
            setError(`Error: ${err.message}`);
        } finally {
            setIsLoading(false);
        }
    };

    const propTypes = [
        { value: 'PTS', label: 'Points', icon: Target },
        { value: 'AST', label: 'Assists', icon: Users },
        { value: 'REB', label: 'Rebounds', icon: TrendingUp },
        { value: 'STL', label: 'Steals', icon: Zap },
        { value: 'BLK', label: 'Blocks', icon: Target },
        { value: '3PM', label: '3-Pointers', icon: Target }
    ];

    const playerCounts = ['1', '2', '3', '4', '5', '6+'];
    const percentages = ['80', '90', '95', '100'];
    const ptsLines = ['10', '15', '20', '25']
    const astLines = ['3', '5', '7', '10']
    const rebLines = ['5', '8', '10', '12']
    const stlLines = ['1', '2', '3', '4']
    const blkLines = ['1', '2', '3', '4']
    const threeLines = ['1', '2', '3', '4']
    const lineMap = {
        PTS: ptsLines,
        AST: astLines,
        REB: rebLines,
        STL: stlLines,
        BLK: blkLines,
        '3PM': threeLines
    };

    // Handler for prop type change
    const handlePropTypeChange = (newPropType) => {
        setPropType(newPropType);
        // Reset stat to first option of the new prop type
        const newLines = lineMap[newPropType];
        if (newLines && newLines.length > 0) {
            setStat(newLines[0]);
        }
    };

    // Get current stat options based on selected prop type
    const currentStatOptions = lineMap[propType] || [];

    return (
        <div>
            <Navbar />
            <div className="min-h-screen flex items-center justify-center bg-gradient-to-r from-slate-900 to-slate-700 p-4">
                <Card className="bg-slate-800 border-slate-700 shadow-2xl w-lg">
                    <CardHeader className="pb-6">
                        <CardTitle className="text-center text-white text-2xl font-bold">
                            Generate Prop Bets
                        </CardTitle>
                        <p className="text-center text-slate-400 text-sm mt-2">
                            Customize your prop bet preferences
                        </p>
                    </CardHeader>
                    <CardContent className="space-y-6">
                        <form onSubmit={handleSubmit} className="space-y-6">
                            {/* Prop Type Selection */}
                            <div className="space-y-3">
                                <label className="text-white font-medium text-sm flex items-center space-x-2">
                                    <Target className="h-4 w-4" />
                                    <span>Prop Type</span>
                                </label>
                                <div className="grid grid-cols-2 gap-3">
                                    {propTypes.map((type) => {
                                        const Icon = type.icon;
                                        return (
                                            <button
                                                key={type.value}
                                                type="button"
                                                onClick={() => handlePropTypeChange(type.value)}
                                                className={`p-3 rounded-lg border-2 transition-all duration-200 flex items-center space-x-2 ${
                                                    propType === type.value
                                                        ? 'border-blue-500 bg-blue-500/20 text-blue-400'
                                                        : 'border-slate-600 bg-slate-700 text-slate-300 hover:border-slate-500'
                                                }`}
                                            >
                                                <Icon className="h-4 w-4" />
                                                <span className="text-sm font-medium">{type.label}</span>
                                            </button>
                                        );
                                    })}
                                </div>
                            </div>

                            {/* Number of Players */}
                            <div className="space-y-3">
                                <label className="text-white font-medium text-sm flex items-center space-x-2">
                                    <Users className="h-4 w-4" />
                                    <span>Number of Players</span>
                                </label>
                                <div className="flex space-x-2">
                                    {playerCounts.map((count) => (
                                        <button
                                            key={count}
                                            type="button"
                                            onClick={() => setNumPlayers(count)}
                                            className={`flex-1 py-2 px-3 rounded-lg border-2 transition-all duration-200 ${
                                                numPlayers === count
                                                    ? 'border-blue-500 bg-blue-500/20 text-blue-400'
                                                    : 'border-slate-600 bg-slate-700 text-slate-300 hover:border-slate-500'
                                            }`}
                                        >
                                            <span className="text-sm font-medium">{count}</span>
                                        </button>
                                    ))}
                                </div>
                            </div>

                            {/* Minimum Percentage */}
                            <div className="space-y-3">
                                <label className="text-white font-medium text-sm flex items-center space-x-2">
                                    <TrendingUp className="h-4 w-4" />
                                    <span>Minimum Success Rate</span>
                                </label>
                                <div className="flex space-x-2">
                                    {percentages.map((percentage) => (
                                        <button
                                            key={percentage}
                                            type="button"
                                            onClick={() => setMinThreshold(percentage)}
                                            className={`flex-1 py-2 px-3 rounded-lg border-2 transition-all duration-200 ${
                                                minThreshold === percentage
                                                    ? 'border-blue-500 bg-blue-500/20 text-blue-400'
                                                    : 'border-slate-600 bg-slate-700 text-slate-300 hover:border-slate-500'
                                            }`}
                                        >
                                            <span className="text-sm font-medium">{percentage}%</span>
                                        </button>
                                    ))}
                                </div>
                            </div>

                            {/* Number of Games */}
                            <div className="space-y-3">
                                <label className="text-white font-medium text-sm flex items-center space-x-2">
                                    <TrendingUp className="h-4 w-4" />
                                    <span>Number of Games to Analyze</span>
                                </label>
                                <div className="flex space-x-2">
                                    {['5', '10', '15', '20'].map((games) => (
                                        <button
                                            key={games}
                                            type="button"
                                            onClick={() => setNumGames(games)}
                                            className={`flex-1 py-2 px-3 rounded-lg border-2 transition-all duration-200 ${
                                                numGames === games
                                                    ? 'border-blue-500 bg-blue-500/20 text-blue-400'
                                                    : 'border-slate-600 bg-slate-700 text-slate-300 hover:border-slate-500'
                                            }`}
                                        >
                                            <span className="text-sm font-medium">{games}</span>
                                        </button>
                                    ))}
                                </div>
                            </div>

                            {/* Stat Threshold*/}
                            <div className="space-y-3">
                                <label className="text-white font-medium text-sm flex items-center space-x-2">
                                    <Target className="h-4 w-4" />
                                    <span>Stat Threshold</span>
                                </label>
                                <div className="flex space-x-2">
                                    {currentStatOptions.map((value) => (
                                        <button
                                            key={value}
                                            type="button"
                                            onClick={() => setStat(value)}
                                            className={`flex-1 py-2 px-3 rounded-lg border-2 transition-all duration-200 ${
                                                stat === value
                                                    ? 'border-blue-500 bg-blue-500/20 text-blue-400'
                                                    : 'border-slate-600 bg-slate-700 text-slate-300 hover:border-slate-500'
                                            }`}
                                        >
                                            <span className="text-sm font-medium">{value}</span>
                                        </button>
                                    ))}
                                </div>
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
                                        <span>Generating Props...</span>
                                    </div>
                                ) : (
                                    <div className="flex items-center justify-center space-x-2">
                                        <Zap className="h-5 w-5" />
                                        <span>Generate Props</span>
                                    </div>
                                )}
                            </Button>
                        </form>

                        {/* Error Message */}
                        {error && (
                            <div className="flex items-center space-x-2 p-4 bg-red-500/20 border border-red-500 rounded-lg">
                                <AlertCircle className="h-5 w-5 text-red-400" />
                                <span className="text-red-400 font-medium">{error}</span>
                            </div>
                        )}

                        {/* Info Section */}
                        <div className="bg-slate-700/50 p-4 rounded-lg">
                            <h3 className="text-white font-medium mb-2">How it works:</h3>
                            <ul className="text-slate-300 text-sm space-y-1">
                                <li>• Select your preferred prop type (Points, Assists, etc.)</li>
                                <li>• Choose number of players for your prop</li>
                                <li>• Set minimum success rate threshold</li>
                                <li>• Get props for today's games</li>
                            </ul>
                        </div>
                    </CardContent>
                </Card>
            </div>
        </div>
    );
};

export default PropBetForm;