
import React, { useState, useEffect, useCallback } from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  PieChart, Pie, Cell // Added PieChart components
} from 'recharts';
import { GraduationCap, Target, Award, ArrowRight, BookOpen, Brain, Zap, Plus, X, CheckCircle, ThumbsUp, Loader2 } from 'lucide-react';

const API_BASE = 'https://course-recom-backend.onrender.com'; // Ensure this matches your FastAPI server address

const LeapCourseMapper = () => {
  // State variables for user inputs
  const [fromSpec, setFromSpec] = useState('');
  const [toSpec, setToSpec] = useState('');
  const [workRoles, setWorkRoles] = useState([]); // Array of { role: string, years: number }

  // State variables for dropdown options fetched from API
  const [specializations, setSpecializations] = useState([]);
  const [allTargets, setAllTargets] = useState([]);
  const [allWorkRoles, setAllWorkRoles] = useState([]);

  // State variables for displaying results
  const [recommendationResult, setRecommendationResult] = useState(null);
  const [breakdownResult, setBreakdownResult] = useState(null);

  // UI state
  const [isLoading, setIsLoading] = useState(true); // For initial data load
  const [isAnalyzing, setIsAnalyzing] = useState(false); // For analysis button state
  const [error, setError] = useState(null);

  // --- Data Fetching on Component Mount ---
  useEffect(() => {
    const fetchData = async () => {
      try {
        const [specsRes, targetsRes, workRolesRes] = await Promise.all([
          fetch(`${API_BASE}/specializations`),
          fetch(`${API_BASE}/targets`),
          fetch(`${API_BASE}/work_roles`)
        ]);

        if (!specsRes.ok || !targetsRes.ok || !workRolesRes.ok) {
          throw new Error('One or more API endpoints failed to load initial data.');
        }

        setSpecializations(await specsRes.json());
        setAllTargets(await targetsRes.json());
        setAllWorkRoles(await workRolesRes.json());
      } catch (err) {
        console.error("Error fetching initial data:", err);
        setError('Failed to load initial data. Please ensure the backend is running and accessible.');
      } finally {
        setIsLoading(false);
      }
    };

    fetchData();
  }, []); // Empty dependency array means this runs once on mount

  // --- Work Roles Management ---
  const addWorkRole = useCallback(() => {
    setWorkRoles(prevRoles => [...prevRoles, { role: '', years: 0 }]);
  }, []);

  const removeWorkRole = useCallback((indexToRemove) => {
    setWorkRoles(prevRoles => prevRoles.filter((_, i) => i !== indexToRemove));
  }, []);

  const updateWorkRole = useCallback((indexToUpdate, field, value) => {
    setWorkRoles(prevRoles =>
      prevRoles.map((role, i) =>
        i === indexToUpdate ? { ...role, [field]: value } : role
      )
    );
  }, []);

  // --- Pathway Analysis ---
  const analyzePathway = async () => {
    // Clear previous results and errors
    setRecommendationResult(null);
    setBreakdownResult(null);
    setError(null);

    // Input validation
    if (!fromSpec) {
      setError('Please select your educational background.');
      return;
    }
    if (!toSpec) {
      setError('Please select your target specialization.');
      return;
    }

    setIsAnalyzing(true);

    try {
      // Format work roles for the API query parameter
      const workRolesParam = workRoles
        .filter(w => w.role) // Only include roles that have been selected
        .map(w => `${encodeURIComponent(w.role)}:${w.years}`) // Encode role names
        .join(',');

      // Construct API URLs
      const recommendUrl = `${API_BASE}/recommend_multi?education_spec=${encodeURIComponent(fromSpec)}&target_spec=${encodeURIComponent(toSpec)}${workRolesParam ? `&work_roles=${workRolesParam}` : ''}`;
      const breakdownUrl = `${API_BASE}/match_breakdown?education_spec=${encodeURIComponent(fromSpec)}&target_spec=${encodeURIComponent(toSpec)}${workRolesParam ? `&work_roles=${workRolesParam}` : ''}`;

      // Fetch data concurrently
      const [recommendRes, breakdownRes] = await Promise.all([
        fetch(recommendUrl),
        fetch(breakdownUrl)
      ]);

      // Handle HTTP errors
      if (!recommendRes.ok) {
        const errData = await recommendRes.json();
        throw new Error(errData.detail?.message || `Recommendation API Error: ${recommendRes.statusText}`);
      }
      if (!breakdownRes.ok) {
        const errData = await breakdownRes.json();
        throw new Error(errData.detail?.message || `Breakdown API Error: ${breakdownRes.statusText}`);
      }

      // Parse JSON responses
      const recommendData = await recommendRes.json();
      const breakdownData = await breakdownRes.json();

      setRecommendationResult(recommendData);
      setBreakdownResult(breakdownData);

    } catch (err) {
      console.error("Analysis failed:", err);
      setError(err.message || 'An unexpected error occurred during analysis. Please try again.');
    } finally {
      setIsAnalyzing(false);
    }
  };

  // --- Helper Functions for UI Rendering ---
  const getMatchTypeColor = (matchType) => {
    switch (matchType) {
      case 'direct': return '#10B981'; // Green
      case 'achievable': return '#3B82F6'; // Blue
      case 'bridge': return '#F59E0B'; // Amber
      case 'fallback': return '#EF4444'; // Red
      default: return '#6B7280'; // Gray
    }
  };

  const getMatchTypeIcon = (matchType) => {
    switch (matchType) {
      case 'direct': return <Target className="w-6 h-6" />;
      case 'achievable': return <Award className="w-6 h-6" />;
      case 'bridge': return <ArrowRight className="w-6 h-6" />;
      case 'fallback': return <BookOpen className="w-6 h-6" />;
      default: return <Brain className="w-6 h-6" />;
    }
  };

  // --- Relevancy Level for Donut Chart ---
  const getRelevancyLevelData = (score) => {
    let level = 'Low';
    let color = '#EF4444'; // Red for Low

    if (score > 75) {
      level = 'High';
      color = '#10B981'; // Green for High
    } else if (score >= 50) { // 50-75
      level = 'Medium';
      color = '#F59E0B'; // Amber for Medium
    }

    // Pie chart data structure
    return {
      data: [{ name: level, value: score }, { name: 'Remaining', value: 100 - score }],
      color: color,
      level: level,
      score: score
    };
  };

  // Custom Label for Pie Chart
  const CustomizedLabel = ({ cx, cy, midAngle, innerRadius, outerRadius, percent, index, value, payload }) => {
    if (payload[0].name === 'Remaining') return null; // Don't label the remaining slice

    const radius = innerRadius + (outerRadius - innerRadius) * 0.5;
    const x = cx + radius * Math.cos(-midAngle * Math.PI / 180);
    const y = cy + radius * Math.sin(-midAngle * Math.PI / 180);

    return (
      <text x={x} y={y} fill="white" textAnchor={x > cx ? 'start' : 'end'} dominantBaseline="central" style={{ fontWeight: 'bold', fontSize: '1.2rem' }}>
        {`${payload[0].value}%`}
      </text>
    );
  };


  // --- Render Components ---

  // Component for 100% Direct Match Special UI
  const renderDirectMatchConfirmation = () => {
    if (!recommendationResult || recommendationResult.match_type !== 'direct' || recommendationResult.score < 100) {
      return null; // Only render if it's a perfect direct match
    }

    return (
      <div style={styles.directMatchCard}>
        <div style={styles.directMatchHeader}>
          <CheckCircle style={styles.directMatchIcon} />
          <div>
            <h2 style={styles.directMatchTitle}>Perfect Match! 🎯</h2>
            <p style={styles.directMatchMessage}>
              Your background in <strong>{recommendationResult.source}</strong> is a perfect match for <strong>{recommendationResult.recommendation}</strong>!
            </p>
          </div>
        </div>

        <div style={styles.directMatchScore}>
          <div style={styles.scoreCircle}>
            <span style={styles.scoreValue}>100</span>
            <span style={styles.scoreLabel}>% Match</span>
          </div>
        </div>

        <div style={styles.directMatchAction}>
          <div style={styles.actionContent}>
            <ThumbsUp style={styles.actionIcon} />
            <div>
              <h3 style={styles.actionTitle}>You're all set!</h3>
              <p style={styles.actionDescription}>
                You can proceed directly to {recommendationResult.recommendation} without any additional preparation or bridge programs.
              </p>
            </div>
          </div>
          <button
            style={styles.proceedButton}
            onMouseEnter={(e) => {
              e.target.style.background = 'rgba(255, 255, 255, 0.3)';
              e.target.style.transform = 'translateY(-2px)';
            }}
            onMouseLeave={(e) => {
              e.target.style.background = 'rgba(255, 255, 255, 0.2)';
              e.target.style.transform = 'translateY(0)';
            }}
          >
            <Target className="w-6 h-6" />
            Proceed to {recommendationResult.recommendation}
          </button>
        </div>
      </div>
    );
  };

  // Component for displaying general recommendation results (not perfect match)
  const renderGeneralRecommendation = () => {
    if (!recommendationResult || (recommendationResult.match_type === 'direct' && recommendationResult.score >= 100)) {
      return null; // Don't render if there's no result or if it's a perfect direct match (handled by specific component)
    }

    const { data: donutData, color: donutColor, level: relevancyLevel, score: currentScore } = getRelevancyLevelData(recommendationResult.score);

    return (
      <div style={styles.resultCard}>
        <div style={styles.matchHeader}>
          <div style={{ color: getMatchTypeColor(recommendationResult.match_type) }}>
            {getMatchTypeIcon(recommendationResult.match_type)}
          </div>
          <div style={{ flex: 1 }}>
            <h3 style={{ margin: 0, fontSize: '1.5rem', fontWeight: '700' }}>
              {recommendationResult.category}
            </h3>
            <p style={{ margin: '0.25rem 0 0 0', color: '#6B7280' }}>
              {recommendationResult.message}
            </p>
          </div>
          <div style={{ ...styles.matchScore, color: getMatchTypeColor(recommendationResult.match_type) }}>
            {recommendationResult.score}%
          </div>
        </div>

        {/* Donut Chart for Relevancy Level */}
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', marginBottom: '1.5rem', flexDirection: 'column' }}>
            <h4 style={{ margin: '0 0 0.5rem 0', fontWeight: '600', color: '#374151' }}>Overall Relevancy Level: {relevancyLevel}</h4>
            <ResponsiveContainer width="100%" height={200}>
                <PieChart>
                    <Pie
                        data={donutData}
                        cx="50%"
                        cy="50%"
                        innerRadius={60}
                        outerRadius={80}
                        fill="#8884d8"
                        paddingAngle={5}
                        dataKey="value"
                        isAnimationActive={false} // Disable animation for static display
                    >
                        {
                            donutData.map((entry, index) => (
                                <Cell key={`cell-${index}`} fill={index === 0 ? donutColor : '#E5E7EB'} />
                            ))
                        }
                    </Pie>
                    <Tooltip />
                    {/* Custom label to show score in the center of the donut */}
                    <text x="50%" y="50%" textAnchor="middle" dominantBaseline="middle" style={{ fontSize: '2em', fontWeight: 'bold', fill: donutColor }}>
                        {`${currentScore}%`}
                    </text>
                    <text x="50%" y="65%" textAnchor="middle" dominantBaseline="middle" style={{ fontSize: '1em', fill: '#6B7280' }}>
                       {relevancyLevel}
                    </text>
                </PieChart>
            </ResponsiveContainer>
        </div>


        {recommendationResult.recommendation && (
          <div style={styles.recommendationBox}>
            <h4 style={{ margin: '0 0 0.5rem 0', fontWeight: '600' }}>
              Recommended Program: {recommendationResult.recommendation}
            </h4>
          </div>
        )}


        {recommendationResult.bridge_programs && recommendationResult.bridge_programs.length > 0 && (
          <div>
            <h4 style={{ margin: '0 0 1rem 0', fontWeight: '600' }}>Bridge Programs:</h4>
            <div style={styles.bridgeGrid}>
              {recommendationResult.bridge_programs.map((program, index) => (
                <div key={index} style={styles.bridgeCard}>
                  <h5 style={{ margin: '0 0 0.5rem 0', fontWeight: '600' }}>{program.name}</h5>
                  <p style={{ margin: 0, color: '#6B7280', fontSize: '0.875rem' }}>
                    Composite Score: {program.composite_score}%
                  </p>
                  <p style={{ margin: '0.25rem 0 0 0', color: '#6B7280', fontSize: '0.75rem' }}>
                    (Relevance to Target: {program.relevance_to_target}%)
                  </p>
                  <p style={{ margin: '0.25rem 0 0 0', color: '#6B7280', fontSize: '0.75rem' }}>
                    (Relevance from Background: {program.relevance_from_background}%)
                  </p>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    );
  };

  // --- Inline Styles ---
  const styles = {
    container: {
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      fontFamily: 'Inter, system-ui, sans-serif',
      padding: '2rem',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
    },
    card: {
      background: 'rgba(255, 255, 255, 0.95)',
      backdropFilter: 'blur(20px)',
      borderRadius: '24px',
      padding: '2rem',
      boxShadow: '0 20px 40px rgba(0, 0, 0, 0.1)',
      border: '1px solid rgba(255, 255, 255, 0.2)',
      maxWidth: '800px',
      width: '100%',
      margin: '0 auto',
      transition: 'transform 0.3s ease-in-out', // Added for subtle hover effect
    },
    header: {
      textAlign: 'center',
      marginBottom: '2rem',
    },
    title: {
      fontSize: '2.5rem',
      fontWeight: '800',
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      WebkitBackgroundClip: 'text',
      WebkitTextFillColor: 'transparent',
      marginBottom: '0.5rem',
    },
    subtitle: {
      fontSize: '1.1rem',
      color: '#6B7280',
      fontWeight: '500',
    },
    inputGroup: {
      marginBottom: '1.5rem',
    },
    label: {
      display: 'block',
      fontSize: '1rem',
      fontWeight: '600',
      color: '#374151',
      marginBottom: '0.5rem',
    },
    select: {
      width: '100%',
      padding: '0.75rem 1rem',
      border: '2px solid #E5E7EB',
      borderRadius: '12px',
      fontSize: '1rem',
      transition: 'all 0.2s',
      outline: 'none',
      backgroundColor: 'white',
      cursor: 'pointer',
    },
    input: { // Unified style for text/number inputs
      width: '100%',
      padding: '0.75rem 1rem',
      border: '2px solid #E5E7EB',
      borderRadius: '12px',
      fontSize: '1rem',
      transition: 'all 0.2s',
      outline: 'none',
      backgroundColor: 'white',
    },
    workRoleContainer: {
      display: 'flex',
      gap: '0.75rem',
      alignItems: 'center',
      marginBottom: '0.75rem',
    },
    workRoleInput: {
      flex: 2,
      padding: '0.75rem 1rem',
      border: '2px solid #E5E7EB',
      borderRadius: '12px',
      fontSize: '1rem',
      outline: 'none',
      backgroundColor: 'white',
      cursor: 'pointer',
    },
    yearsInput: {
      flex: 1,
      padding: '0.75rem 1rem',
      border: '2px solid #E5E7EB',
      borderRadius: '12px',
      fontSize: '1rem',
      outline: 'none',
      backgroundColor: 'white',
      minWidth: '80px',
    },
    button: {
      background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
      color: 'white',
      border: 'none',
      padding: '0.75rem 1.5rem',
      borderRadius: '12px',
      fontSize: '1rem',
      fontWeight: '600',
      cursor: 'pointer',
      display: 'flex',
      alignItems: 'center',
      gap: '0.5rem',
      transition: 'all 0.2s',
      width: '100%',
      justifyContent: 'center',
    },
    addButton: {
      background: '#10B981',
      color: 'white',
      border: 'none',
      padding: '0.5rem',
      borderRadius: '8px',
      cursor: 'pointer',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      transition: 'all 0.2s',
      alignSelf: 'flex-start',
    },
    removeButton: {
      background: '#EF4444',
      color: 'white',
      border: 'none',
      padding: '0.5rem',
      borderRadius: '8px',
      cursor: 'pointer',
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      transition: 'all 0.2s',
      flexShrink: 0,
    },
    resultCard: {
      background: 'rgba(255, 255, 255, 0.95)',
      backdropFilter: 'blur(20px)',
      borderRadius: '24px',
      padding: '2rem',
      boxShadow: '0 20px 40px rgba(0, 0, 0, 0.1)',
      border: '1px solid rgba(255, 255, 255, 0.2)',
      maxWidth: '800px',
      width: '100%',
      margin: '2rem auto',
      transition: 'transform 0.3s ease-in-out', // Added for subtle hover effect
    },
    matchHeader: {
      display: 'flex',
      alignItems: 'center',
      gap: '1rem',
      marginBottom: '1.5rem',
    },
    matchScore: {
      fontSize: '2rem',
      fontWeight: '800',
      marginLeft: 'auto',
    },
    recommendationBox: {
      background: '#F3F4F6',
      borderRadius: '12px',
      padding: '1rem',
      marginBottom: '1rem',
    },
    bridgeGrid: {
      display: 'grid',
      gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))',
      gap: '1rem',
      marginTop: '1rem',
    },
    bridgeCard: {
      background: 'rgba(249, 250, 251, 0.8)',
      border: '1px solid #E5E7EB',
      borderRadius: '12px',
      padding: '1rem',
      textAlign: 'center',
      transition: 'all 0.2s',
      display: 'flex',
      flexDirection: 'column',
      justifyContent: 'center',
    },
    error: {
      background: '#FEF2F2',
      color: '#DC2626',
      border: '1px solid #FECACA',
      borderRadius: '12px',
      padding: '1rem',
      marginBottom: '1rem',
      textAlign: 'center',
    },
    // Direct Match Confirmation Styles
    directMatchCard: {
      background: 'linear-gradient(135deg, #10B981 0%, #059669 100%)',
      borderRadius: '24px',
      padding: '2.5rem',
      boxShadow: '0 20px 40px rgba(16, 185, 129, 0.3)',
      maxWidth: '800px',
      width: '100%',
      margin: '2rem auto',
      color: 'white',
      position: 'relative',
      overflow: 'hidden',
      textAlign: 'center',
      transition: 'transform 0.3s ease-in-out',
    },
    directMatchHeader: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '1rem',
      marginBottom: '2rem',
    },
    directMatchIcon: {
      width: '64px',
      height: '64px',
      color: 'white',
    },
    directMatchTitle: {
      fontSize: '2.5rem',
      fontWeight: '800',
      margin: '0 0 0.5rem 0',
      color: 'white',
    },
    directMatchMessage: {
      fontSize: '1.2rem',
      margin: 0,
      opacity: 0.9,
    },
    directMatchScore: {
      display: 'flex',
      justifyContent: 'center',
      marginBottom: '2rem',
    },
    scoreCircle: {
      width: '140px',
      height: '140px',
      borderRadius: '50%',
      background: 'rgba(255, 255, 255, 0.2)',
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      border: '3px solid rgba(255, 255, 255, 0.3)',
    },
    scoreValue: {
      fontSize: '3rem',
      fontWeight: '900',
      color: 'white',
      lineHeight: 1,
    },
    scoreLabel: {
      fontSize: '1rem',
      fontWeight: '600',
      color: 'white',
      opacity: 0.8,
    },
    directMatchAction: {
      background: 'rgba(255, 255, 255, 0.1)',
      borderRadius: '16px',
      padding: '1.5rem',
      backdropFilter: 'blur(10px)',
    },
    actionContent: {
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      gap: '1rem',
      marginBottom: '1rem',
    },
    actionIcon: {
      width: '32px',
      height: '32px',
      color: 'white',
    },
    actionTitle: {
      fontSize: '1.5rem',
      fontWeight: '700',
      margin: '0 0 0.25rem 0',
      color: 'white',
    },
    actionDescription: {
      fontSize: '1rem',
      margin: 0,
      opacity: 0.9,
    },
    proceedButton: {
      background: 'rgba(255, 255, 255, 0.2)',
      color: 'white',
      border: '2px solid rgba(255, 255, 255, 0.3)',
      padding: '0.75rem 1.5rem',
      borderRadius: '12px',
      fontSize: '1rem',
      fontWeight: '600',
      cursor: 'pointer',
      display: 'flex',
      alignItems: 'center',
      gap: '0.5rem',
      transition: 'all 0.2s',
      width: '100%',
      justifyContent: 'center',
    },
    loadingOverlay: {
      position: 'fixed',
      top: 0,
      left: 0,
      right: 0,
      bottom: 0,
      backgroundColor: 'rgba(0, 0, 0, 0.5)',
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      zIndex: 1000,
      color: 'white',
      fontSize: '1.2rem',
      flexDirection: 'column',
      gap: '1rem',
    },
  };

  if (isLoading) {
    return (
      <div style={styles.loadingOverlay}>
        <Loader2 className="w-12 h-12 animate-spin" />
        Loading application data...
      </div>
    );
  }

  return (
    <div style={styles.container}>
      <div style={styles.card}>
        <div style={styles.header}>
          <h1 style={styles.title}>LeapCourse Mapper</h1>
          <p style={styles.subtitle}>
            Discover your optimal academic and career pathway with AI-powered recommendations
          </p>
        </div>

        {error && (
          <div style={styles.error}>
            {error}
          </div>
        )}

        <div style={styles.inputGroup}>
          <label style={styles.label}>
            <GraduationCap className="inline w-5 h-5 mr-2" />
            Educational Background
          </label>
          <select
            style={styles.select}
            value={fromSpec}
            onChange={(e) => setFromSpec(e.target.value)}
            onFocus={(e) => {
              e.target.style.borderColor = '#667eea';
              e.target.style.boxShadow = '0 0 0 3px rgba(102, 126, 234, 0.1)';
            }}
            onBlur={(e) => {
              e.target.style.borderColor = '#E5E7EB';
              e.target.style.boxShadow = 'none';
            }}
            disabled={isAnalyzing}
          >
            <option value="">Select your educational specialization</option>
            {specializations.map(spec => (
              <option key={spec} value={spec}>{spec}</option>
            ))}
          </select>
        </div>

        <div style={styles.inputGroup}>
          <label style={styles.label}>
            <Brain className="inline w-5 h-5 mr-2" />
            Work Experience (Optional)
          </label>
          {workRoles.map((role, index) => (
            <div key={index} style={styles.workRoleContainer}>
              <select
                style={styles.workRoleInput}
                value={role.role}
                onChange={(e) => updateWorkRole(index, 'role', e.target.value)}
                onFocus={(e) => {
                  e.target.style.borderColor = '#667eea';
                  e.target.style.boxShadow = '0 0 0 3px rgba(102, 126, 234, 0.1)';
                }}
                onBlur={(e) => {
                  e.target.style.borderColor = '#E5E7EB';
                  e.target.style.boxShadow = 'none';
                }}
                disabled={isAnalyzing}
              >
                <option value="">Select work role</option>
                {allWorkRoles.map(workRole => (
                  <option key={workRole} value={workRole}>{workRole}</option>
                ))}
              </select>
              <input
                type="number"
                style={styles.yearsInput}
                placeholder="Years"
                value={role.years}
                onChange={(e) => updateWorkRole(index, 'years', parseInt(e.target.value) || 0)}
                onFocus={(e) => {
                  e.target.style.borderColor = '#667eea';
                  e.target.style.boxShadow = '0 0 0 3px rgba(102, 126, 234, 0.1)';
                }}
                onBlur={(e) => {
                  e.target.style.borderColor = '#E5E7EB';
                  e.target.style.boxShadow = 'none';
                }}
                min="0"
                max="50"
                disabled={isAnalyzing}
              />
              <button
                style={styles.removeButton}
                onClick={() => removeWorkRole(index)}
                onMouseEnter={(e) => {
                  e.target.style.transform = 'translateY(-1px)';
                  e.target.style.boxShadow = '0 4px 8px rgba(239, 68, 68, 0.3)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.transform = 'translateY(0)';
                  e.target.style.boxShadow = 'none';
                }}
                disabled={isAnalyzing}
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          ))}
          <button
            style={styles.addButton}
            onClick={addWorkRole}
            onMouseEnter={(e) => {
              e.target.style.transform = 'translateY(-1px)';
              e.target.style.boxShadow = '0 4px 8px rgba(16, 185, 129, 0.3)';
            }}
            onMouseLeave={(e) => {
              e.target.style.transform = 'translateY(0)';
              e.target.style.boxShadow = 'none';
            }}
            disabled={isAnalyzing}
          >
            <Plus className="w-4 h-4" />
          </button>
        </div>

        <div style={styles.inputGroup}>
          <label style={styles.label}>
            <Target className="inline w-5 h-5 mr-2" />
            Target Specialization
          </label>
          <select
            style={styles.select}
            value={toSpec}
            onChange={(e) => setToSpec(e.target.value)}
            onFocus={(e) => {
              e.target.style.borderColor = '#667eea';
              e.target.style.boxShadow = '0 0 0 3px rgba(102, 126, 234, 0.1)';
            }}
            onBlur={(e) => {
              e.target.style.borderColor = '#E5E7EB';
              e.target.style.boxShadow = 'none';
            }}
            disabled={isAnalyzing}
          >
            <option value="">Select your target specialization</option>
            {allTargets.map(target => (
              <option key={target} value={target}>{target}</option>
            ))}
          </select>
        </div>

        <button
          style={{
            ...styles.button,
            opacity: (isAnalyzing || !fromSpec || !toSpec) ? 0.6 : 1,
            cursor: (isAnalyzing || !fromSpec || !toSpec) ? 'not-allowed' : 'pointer',
          }}
          onClick={analyzePathway}
          disabled={isAnalyzing || !fromSpec || !toSpec}
          onMouseEnter={(e) => {
            if (!isAnalyzing && fromSpec && toSpec) {
              e.target.style.transform = 'translateY(-2px)';
              e.target.style.boxShadow = '0 10px 20px rgba(102, 126, 234, 0.3)';
            }
          }}
          onMouseLeave={(e) => {
            if (!isAnalyzing && fromSpec && toSpec) {
              e.target.style.transform = 'translateY(0)';
              e.target.style.boxShadow = 'none';
            }
          }}
        >
          {isAnalyzing ? (
            <>
              <Loader2 className="w-5 h-5 animate-spin" />
              Analyzing Pathway...
            </>
          ) : (
            <>
              <Brain className="w-5 h-5" />
              Analyze Pathway
            </>
          )}
        </button>
      </div>

      {/* Render the specific direct match confirmation or general recommendation */}
      {recommendationResult && (recommendationResult.match_type === 'direct' && recommendationResult.score >= 100
        ? renderDirectMatchConfirmation()
        : renderGeneralRecommendation()
      )}

      {/* Render Breakdown Chart only if not a perfect direct match */}
      {breakdownResult && !(recommendationResult?.match_type === 'direct' && recommendationResult?.score >= 100) && (
        <div style={styles.resultCard}>
          <h3 style={{ margin: '0 0 1rem 0', fontSize: '1.5rem', fontWeight: '700' }}>
            Background Analysis
          </h3>
          <div style={{ marginBottom: '1rem' }}>
            <ResponsiveContainer width="100%" height={300}>
              <BarChart data={breakdownResult.breakdown}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="original_input" angle={-45} textAnchor="end" height={80} interval={0} />
                <YAxis label={{ value: 'Relevancy Score (%)', angle: -90, position: 'insideLeft' }} />
                <Tooltip />
                <Bar dataKey="score" fill="#667eea" />
              </BarChart>
            </ResponsiveContainer>
          </div>
          <div style={styles.bridgeGrid}>
            {breakdownResult.breakdown.map((item, index) => (
              <div
                key={index}
                style={styles.bridgeCard}
                onMouseEnter={(e) => {
                  e.target.style.transform = 'translateY(-2px)';
                  e.target.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.1)';
                }}
                onMouseLeave={(e) => {
                  e.target.style.transform = 'translateY(0)';
                  e.target.style.boxShadow = 'none';
                }}
              >
                <h5 style={{ margin: '0 0 0.5rem 0', fontWeight: '600' }}>{item.type}</h5>
                <p style={{ margin: '0 0 0.25rem 0', fontSize: '0.875rem' }}>
                  {item.original_input} {item.specialization_matched !== item.original_input && item.specialization_matched !== "N/A" && `(Mapped to: ${item.specialization_matched})`}
                </p>
                <p style={{ margin: '0 0 0.25rem 0', color: '#6B7280', fontSize: '0.875rem' }}>
                  Score: {item.score}% | Level: {item.match_level}
                </p>
                {item.years > 0 && (
                  <p style={{ margin: 0, color: '#6B7280', fontSize: '0.875rem' }}>
                    Experience: {item.years} years
                  </p>
                )}
                {item.message && (
                  <p style={{ margin: '0.5rem 0 0 0', color: '#EF4444', fontSize: '0.75rem' }}>
                    {item.message}
                  </p>
                )}
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default LeapCourseMapper;
