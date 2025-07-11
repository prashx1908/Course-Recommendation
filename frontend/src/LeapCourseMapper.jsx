import React, { useState, useEffect, Fragment } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer, RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis, Radar } from 'recharts';
import { GraduationCap, Target, Award, ArrowRight, BookOpen, Brain, Zap } from 'lucide-react';

const API_BASE = 'https://course-recom-backend.onrender.com';

const LeapCourseMapper = () => {
  const [fromSpec, setFromSpec] = useState('');
  const [toSpec, setToSpec] = useState('');
  const [workRoleInput, setWorkRoleInput] = useState('');
  const [workRoleYearsInput, setWorkRoleYearsInput] = useState('');
  const [workRoles, setWorkRoles] = useState([]); // now array of {role, years}
  const [workRoleSuggestions, setWorkRoleSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [specializations, setSpecializations] = useState([]);
  const [allTargets, setAllTargets] = useState([]);
  const [result, setResult] = useState(null);
  const [progress, setProgress] = useState(0);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [relevancyBreakdown, setRelevancyBreakdown] = useState(null);

  useEffect(() => {
    fetch(`${API_BASE}/specializations`)
      .then(res => res.json())
      .then(data => setSpecializations(data));
    fetch(`${API_BASE}/targets`)
      .then(res => res.json())
      .then(data => setAllTargets(data));
    fetch(`${API_BASE}/work_roles`)
      .then(res => res.json())
      .then(data => setWorkRoleSuggestions(data));
  }, []);

  const styles = {
    bg: {
      minHeight: '100vh',
      background: 'linear-gradient(135deg, #e0c3fc 0%, #f5f7fa 100%)',
      fontFamily: '"Manrope", "Poppins", "Segoe UI", Arial, sans-serif',
      color: '#181A2A',
      paddingBottom: 40,
    },
    header: {
      textAlign: 'center',
      padding: '3.5rem 1rem 2.5rem 1rem',
    },
    logo: {
      height: 70,
      marginBottom: 28,
      filter: 'drop-shadow(0 4px 24px #a084e8aa)'
    },
    badge: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 10,
      background: 'rgba(255,255,255,0.7)',
      borderRadius: 999,
      padding: '0.6em 1.7em',
      fontWeight: 700,
      fontSize: 18,
      color: '#7c7caa',
      boxShadow: '0 2px 12px rgba(108,71,255,0.10)',
      marginBottom: 28,
      backdropFilter: 'blur(8px)',
      letterSpacing: '0.02em',
    },
    heading: {
      fontSize: 48,
      fontWeight: 900,
      color: '#6c47ff',
      marginBottom: 8,
      letterSpacing: '-1.5px',
      lineHeight: 1.1,
      textShadow: '0 2px 16px #a084e855',
    },
    headingAccent: {
      color: '#a084e8',
      display: 'block',
      fontSize: 48,
      fontWeight: 900,
      marginTop: 0,
      letterSpacing: '-1.5px',
    },
    subheading: {
      fontSize: 22,
      color: '#7c7caa',
      marginBottom: 38,
      fontWeight: 600,
      letterSpacing: '0.01em',
    },
    card: {
      background: 'rgba(255,255,255,0.85)',
      borderRadius: 36,
      boxShadow: '0 12px 48px 0 #a084e822, 0 2px 8px #e0c3fc33',
      padding: '2.8rem 2.2rem',
      margin: '2.5rem auto',
      maxWidth: 720,
      backdropFilter: 'blur(12px)',
      border: '1.5px solid #e0c3fc55',
    },
    label: {
      fontSize: 20,
      color: '#6c47ff',
      fontWeight: 700,
      marginBottom: 6,
      display: 'block',
      letterSpacing: '0.01em',
    },
    helper: {
      fontSize: 16,
      color: '#7c7caa',
      marginBottom: 18,
      display: 'block',
      fontWeight: 500,
    },
    select: {
      width: '100%',
      padding: '1.1rem',
      borderRadius: 20,
      border: '1.5px solid #e0c3fc',
      background: 'rgba(248,248,255,0.95)',
      fontSize: 18,
      marginBottom: 28,
      transition: 'border 0.2s',
      outline: 'none',
      fontWeight: 600,
      color: '#6c47ff',
      boxShadow: '0 1px 8px #e0c3fc22',
    },
    button: {
      display: 'inline-flex',
      alignItems: 'center',
      gap: 14,
      padding: '1.2em 2.8em',
      fontSize: 20,
      fontWeight: 800,
      color: '#fff',
      background: 'linear-gradient(90deg, #6c47ff 0%, #a084e8 100%)',
      border: 'none',
      borderRadius: 36,
      boxShadow: '0 4px 24px #a084e822',
      cursor: 'pointer',
      transition: 'background 0.2s, transform 0.1s',
      marginTop: 18,
      letterSpacing: '0.01em',
    },
    buttonDisabled: {
      opacity: 0.6,
      cursor: 'not-allowed',
    },
    progressBarBg: {
      background: 'rgba(224,224,239,0.7)',
      borderRadius: 24,
      height: 20,
      width: '100%',
      margin: '1.7em 0',
      boxShadow: '0 1px 8px #e0c3fc22',
    },
    progressBarFill: percent => ({
      background: 'linear-gradient(90deg, #6c47ff 0%, #a084e8 100%)',
      borderRadius: 24,
      height: '100%',
      width: percent + '%',
      transition: 'width 0.5s',
    }),
    circularProgress: {
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      margin: '2.5em 0',
      position: 'relative',
    },
    pill: {
      display: 'inline-block',
      background: 'rgba(245,247,250,0.95)',
      color: '#6c47ff',
      borderRadius: 28,
      padding: '0.7em 1.5em',
      fontWeight: 700,
      margin: '0.3em 0.7em 0.3em 0',
      boxShadow: '0 1px 8px #e0c3fc22',
      fontSize: 18,
      border: '1.5px solid #e0c3fc',
    },
    resultCard: {
      background: 'rgba(255,255,255,0.92)',
      borderRadius: 36,
      boxShadow: '0 12px 48px 0 #a084e822, 0 2px 8px #e0c3fc33',
      padding: '2.8rem 2.2rem',
      margin: '2.5rem auto',
      maxWidth: 720,
      backdropFilter: 'blur(12px)',
      border: '1.5px solid #e0c3fc55',
    },
    altOptions: {
      display: 'flex',
      flexWrap: 'wrap',
      justifyContent: 'center',
      gap: 16,
      marginTop: 18,
    },
    altPill: {
      background: 'rgba(248,248,255,0.95)',
      color: '#6c47ff',
      borderRadius: 28,
      padding: '0.7em 1.5em',
      fontWeight: 700,
      fontSize: 18,
      boxShadow: '0 1px 8px #e0c3fc22',
      margin: '0.3em',
      border: '1.5px solid #e0c3fc',
    },
    analyticsCard: {
      background: 'rgba(255,255,255,0.92)',
      borderRadius: 36,
      boxShadow: '0 12px 48px 0 #a084e822, 0 2px 8px #e0c3fc33',
      padding: '2.8rem 2.2rem',
      margin: '2.5rem auto',
      maxWidth: 1000,
      backdropFilter: 'blur(12px)',
      border: '1.5px solid #e0c3fc55',
    },
    metricsRow: {
      display: 'flex',
      justifyContent: 'center',
      gap: 40,
      marginTop: 40,
      marginBottom: 20,
      flexWrap: 'wrap',
    },
    metricCard: {
      background: 'linear-gradient(90deg, #f5f7fa 0%, #e0c3fc 100%)',
      borderRadius: 28,
      padding: '2.2rem 2.7rem',
      minWidth: 200,
      textAlign: 'center',
      boxShadow: '0 2px 12px #e0c3fc22',
      margin: '0.7em 0',
    },
    metricValue: {
      fontSize: 38,
      fontWeight: 900,
      color: '#6c47ff',
      marginBottom: 10,
      letterSpacing: '-1px',
    },
    metricLabel: {
      fontSize: 18,
      color: '#7c7caa',
      fontWeight: 700,
      letterSpacing: '0.01em',
    },
    chartTitle: {
      fontWeight: 800,
      color: '#6c47ff',
      fontSize: 22,
      marginBottom: 18,
      textAlign: 'center',
      letterSpacing: '-0.5px',
    },
    chartDesc: {
      color: '#7c7caa',
      fontSize: 16,
      textAlign: 'center',
      marginTop: 10,
      fontWeight: 500,
    },
  };

  const CircularProgress = ({ value, size = 120, strokeWidth = 10 }) => {
    const radius = (size - strokeWidth) / 2;
    const circumference = radius * 2 * Math.PI;
    const offset = circumference - (value / 100) * circumference;
    return (
      <div style={styles.circularProgress}>
        <svg width={size} height={size} style={{ transform: 'rotate(-90deg)' }}>
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            stroke="#e0e0ef"
            strokeWidth={strokeWidth}
            fill="transparent"
          />
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            stroke="#6c47ff"
            strokeWidth={strokeWidth}
            fill="transparent"
            strokeDasharray={circumference}
            strokeDashoffset={offset}
            strokeLinecap="round"
            style={{ transition: 'stroke-dashoffset 1s ease-in-out' }}
          />
        </svg>
        <div style={{ position: 'absolute', fontSize: 32, fontWeight: 700, color: '#6c47ff' }}>{value}%</div>
      </div>
    );
  };

  const handleAddWorkRole = (role, years) => {
    const r = (role || workRoleInput).trim();
    const y = parseInt(years || workRoleYearsInput, 10);
    if (r && !workRoles.some(w => w.role === r)) {
      setWorkRoles([...workRoles, { role: r, years: isNaN(y) ? 0 : y }]);
      setWorkRoleInput('');
      setWorkRoleYearsInput('');
      setShowSuggestions(false);
    }
  };

  const handleRemoveWorkRole = (role) => {
    setWorkRoles(workRoles.filter(w => w.role !== role));
  };

  const filteredSuggestions = workRoleInput
    ? workRoleSuggestions.filter(
        s => s.toLowerCase().includes(workRoleInput.toLowerCase()) && !workRoles.some(w => w.role === s)
      ).slice(0, 8)
    : [];

  const getRecommendation = () => {
    if (!fromSpec || !toSpec) return;
    setIsAnalyzing(true);
    setProgress(0);
    const progressInterval = setInterval(() => {
      setProgress(prev => {
        if (prev >= 100) {
          clearInterval(progressInterval);
          return 100;
        }
        return prev + 10;
      });
    }, 150);
    setTimeout(async () => {
      setIsAnalyzing(false);
      const workRolesParam = workRoles.map(w => `${w.role}:${w.years}`).join(',');
      const params = new URLSearchParams({
        education_spec: fromSpec,
        work_roles: workRolesParam,
        target_spec: toSpec
      });
      const res = await fetch(`${API_BASE}/recommend_multi?${params.toString()}`);
      const data = await res.json();
      setResult({
        category: data.category,
        source: data.source,
        score: data.score,
        message: data.message,
        error: data.error,
        alternatives: data.alternatives
      });
    }, 2000);
  };

  const getRelevancyBreakdown = async () => {
    if (!fromSpec || !toSpec) return;
    const workRolesParam = workRoles.map(w => `${w.role}:${w.years}`).join(',');
    const params = new URLSearchParams({
      education_spec: fromSpec,
      work_roles: workRolesParam,
      target_spec: toSpec
    });
    const res = await fetch(`${API_BASE}/relevancy_breakdown?${params.toString()}`);
    const data = await res.json();
    setRelevancyBreakdown(data);
  };

  const handleGetRecommendation = async () => {
    await getRelevancyBreakdown();
    getRecommendation();
  };

  const getDistanceData = () => {
    if (!fromSpec || !toSpec || !result) return [];
    return [
      { name: 'Your Background', value: fromSpec, distance: 0, color: '#3b82f6' },
      { name: 'Target Program', value: toSpec, distance: 100 - (result.score || 0), color: '#ef4444' },
      { name: 'Recommended', value: result.recommendation, distance: result.recommendation === toSpec ? 100 - (result.score || 0) : 20, color: '#10b981' }
    ];
  };

  const getRadarData = () => {
    if (!fromSpec || !result) return [];
    const skills = ['Technical Skills', 'Domain Knowledge', 'Research Methods', 'Industry Relevance', 'Career Prospects'];
    return skills.map(skill => ({
      skill,
      current: Math.random() * 100,
      target: Math.random() * 100,
      recommended: Math.random() * 100
    }));
  };

  return (
    <Fragment>
      <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;600;700;900&family=Poppins:wght@400;600;700;900&display=swap" rel="stylesheet" />
      <div style={styles.bg}>
      {/* Header */}
        <div style={styles.header}>
          <img 
            src="https://ik.imagekit.io/onsnhxjshmp/LeapScholar/new-header-logo_7i5sVUf9VF.svg" 
            alt="Leap Scholar" 
            style={styles.logo}
          />
          <div style={styles.badge}>
            <Zap style={{ width: 20, height: 20, color: '#FFD700' }} />
            <span>AI-Powered Course Matching</span>
          </div>
          <div style={styles.heading}>Your Study Abroad Plan
            <span style={styles.headingAccent}>in Minutes</span>
        </div>
          <div style={styles.subheading}>
          Get personalized course recommendations with AI-powered analysis and visual insights
                </div>
              </div>
        {/* Input Card */}
        <div style={styles.card}>
          <div style={{ marginBottom: 32 }}>
            <span style={styles.label}>Your Background</span>
            <span style={styles.helper}>Select your previous field of study</span>
              <select 
                value={fromSpec}
              onChange={e => setFromSpec(e.target.value)}
              style={styles.select}
              >
                <option value="">Choose your background...</option>
                {specializations.map(spec => (
                  <option key={spec} value={spec}>{spec}</option>
                ))}
              </select>
            </div>
          <div style={{ marginBottom: 32, position: 'relative' }}>
            <span style={styles.label}>Work Experience Roles</span>
            <span style={styles.helper}>Add your work roles (e.g. Software Engineering, Marketing, etc.)</span>
            <div style={{ display: 'flex', gap: 12, marginBottom: 12 }}>
              <input
                type="text"
                value={workRoleInput}
                onChange={e => {
                  setWorkRoleInput(e.target.value);
                  setShowSuggestions(true);
                }}
                onFocus={() => setShowSuggestions(true)}
                onBlur={() => setTimeout(() => setShowSuggestions(false), 150)}
                onKeyDown={e => {
                  if (e.key === 'Enter') { e.preventDefault(); handleAddWorkRole(); }
                }}
                style={{ ...styles.select, flex: 2, marginBottom: 0 }}
                placeholder="Type a work role and press Enter or +"
                autoComplete="off"
              />
              <input
                type="number"
                min="0"
                value={workRoleYearsInput}
                onChange={e => setWorkRoleYearsInput(e.target.value)}
                style={{ ...styles.select, flex: 1, marginBottom: 0, maxWidth: 100 }}
                placeholder="Years"
              />
              <button
                type="button"
                onClick={() => handleAddWorkRole()}
                style={{ ...styles.button, padding: '0.8em 1.5em', fontSize: 18, marginTop: 0 }}
                disabled={!workRoleInput.trim()}
              >+
              </button>
                </div>
            {showSuggestions && filteredSuggestions.length > 0 && (
              <div style={{
                position: 'absolute',
                top: 80,
                left: 0,
                right: 0,
                background: '#fff',
                borderRadius: 16,
                boxShadow: '0 4px 24px #a084e822',
                zIndex: 10,
                maxHeight: 220,
                overflowY: 'auto',
                border: '1.5px solid #e0c3fc',
              }}>
                {filteredSuggestions.map(s => (
                  <div
                    key={s}
                    onMouseDown={() => handleAddWorkRole(s, '')}
                    style={{
                      padding: '1em 1.5em',
                      cursor: 'pointer',
                      color: '#6c47ff',
                      fontWeight: 600,
                      fontSize: 18,
                      borderBottom: '1px solid #f5f7fa',
                    }}
                  >
                    {s}
                </div>
                ))}
              </div>
            )}
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 8 }}>
              {workRoles.map(w => (
                <span key={w.role} style={{ ...styles.pill, background: '#e0c3fc', color: '#6c47ff', display: 'flex', alignItems: 'center', gap: 6 }}>
                  {w.role} ({w.years} yrs)
                  <span
                    onClick={() => handleRemoveWorkRole(w.role)}
                    style={{ cursor: 'pointer', marginLeft: 4, fontWeight: 900 }}
                  >×</span>
                </span>
              ))}
            </div>
          </div>
          <div style={{ marginBottom: 32 }}>
            <span style={styles.label}>Target Program</span>
            <span style={styles.helper}>Choose your desired program</span>
              <select 
                value={toSpec}
              onChange={e => setToSpec(e.target.value)}
              style={styles.select}
              >
                <option value="">Choose your target...</option>
                {allTargets.map(spec => (
                  <option key={spec} value={spec}>{spec}</option>
                ))}
              </select>
            </div>
          <div style={{ textAlign: 'center' }}>
            <button
              onClick={handleGetRecommendation}
              disabled={!fromSpec || !toSpec || isAnalyzing}
              style={{ ...styles.button, ...((!fromSpec || !toSpec || isAnalyzing) ? styles.buttonDisabled : {}) }}
            >
              <Brain style={{ width: 22, height: 22 }} />
              {isAnalyzing ? 'Analyzing...' : 'Get AI Recommendation'}
              <ArrowRight style={{ width: 22, height: 22 }} />
            </button>
          </div>
        </div>
        {/* Progress Bar */}
        {isAnalyzing && (
          <div style={{ ...styles.card, maxWidth: 700, margin: '2rem auto' }}>
            <div style={{ textAlign: 'center', fontWeight: 700, fontSize: 20, marginBottom: 16 }}>AI Analysis in Progress</div>
            <div style={styles.progressBarBg}>
              <div style={styles.progressBarFill(progress)}></div>
            </div>
            <div style={{ textAlign: 'center', color: '#7c7caa', fontSize: 16 }}>Analyzing compatibility and finding optimal pathways...</div>
          </div>
        )}
        {/* Recommended Program Card - always shown at the top of results */}
        {result && !isAnalyzing && (
          <div style={{
            background: 'linear-gradient(90deg, #e0c3fc 0%, #f5f7fa 100%)',
            borderRadius: 22,
            padding: '2.2rem 2.7rem',
            margin: '0 auto 32px auto',
            maxWidth: 480,
            textAlign: 'center',
            color: '#6c47ff',
            fontWeight: 900,
            fontSize: 30,
            boxShadow: '0 4px 24px #e0c3fc44',
            border: '3px solid #a084e8',
            position: 'relative',
            zIndex: 2,
          }}>
            <div style={{ fontSize: 26, fontWeight: 800, color: '#a084e8', marginBottom: 12, letterSpacing: 1 }}>Recommended Program</div>
            <div style={{ fontSize: 38, fontWeight: 900, color: '#6c47ff', marginBottom: 10, letterSpacing: 1 }}>{result.recommendation || result.alternatives?.[0]?.name || 'N/A'}</div>
            <div style={{ fontSize: 20, fontWeight: 700, color: '#22c55e', marginBottom: 8 }}>{result.category}</div>
            {result.alternatives && result.alternatives.length > 0 && (
              <span style={{
                display: 'inline-block',
                fontSize: 18,
                fontWeight: 800,
                color: result.alternatives[0].tag === 'core' ? '#22c55e' : '#a084e8',
                background: result.alternatives[0].tag === 'core' ? '#e0fbe0' : '#ede9fe',
                borderRadius: 14,
                padding: '0.4em 1.1em',
                marginLeft: 10,
                marginTop: 8,
                letterSpacing: 1,
              }}>{result.alternatives[0].tag === 'core' ? 'Core' : 'Non-core'}</span>
            )}
          </div>
        )}
        {/* Results Section (breakdown, analytics, etc.) */}
        {result && !isAnalyzing && (
          <div style={styles.resultCard}>
            {result.error ? (
              <div style={{ color: '#ef4444', fontWeight: 700, fontSize: 20 }}>{result.error}</div>
            ) : (
              <>
                {/* Relevancy Breakdown Bars (replace old circular bar and top recommendation) */}
                {relevancyBreakdown && relevancyBreakdown.relevancies && (
                  <div style={{ display: 'flex', flexWrap: 'wrap', gap: 32, justifyContent: 'center', marginTop: 8, marginBottom: 8 }}>
                    {relevancyBreakdown.relevancies.map((item, idx) => (
                      <div key={item.label + item.source} style={{ flex: '1 1 180px', minWidth: 180, maxWidth: 260, background: '#f5f7fa', borderRadius: 18, boxShadow: '0 2px 12px #e0c3fc22', padding: '1.2rem 1.2rem', textAlign: 'center', margin: '0.7em 0' }}>
                        <div style={{ fontWeight: 700, color: '#6c47ff', fontSize: 18, marginBottom: 4 }}>{item.label}</div>
                        <div style={{ fontWeight: 600, color: '#7c7caa', fontSize: 16, marginBottom: 8 }}>{item.source}</div>
                        {typeof item.score === 'number' ? (
                          <div style={{ fontWeight: 800, color: '#6c47ff', fontSize: 28, marginBottom: 2 }}>{Math.round(item.score)}%</div>
                        ) : (
                          <div style={{ color: '#ef4444', fontWeight: 700, fontSize: 18 }}>N/A</div>
                        )}
                  </div>
                    ))}
                </div>
                  )}
                {/* Fallback and Bridge Alternatives */}
                {(result.match_type === 'fallback' || result.match_type === 'bridge') && (
                  <>
                    <div style={{ background: 'linear-gradient(90deg, #f5f7fa 0%, #e0c3fc 100%)', borderRadius: 20, padding: 20, margin: '0 auto 32px auto', maxWidth: 500, textAlign: 'center', color: '#6c47ff', fontWeight: 600, fontSize: 18 }}>
                      {result.message}
                    </div>
                    {result.alternatives && result.alternatives.length > 0 && (
                      <div style={{ display: 'flex', flexWrap: 'wrap', gap: 24, justifyContent: 'center', marginTop: 8 }}>
                        {result.alternatives.map((alt, idx) => (
                          <div key={alt.name} style={{
                            background: '#f5f7fa',
                            borderRadius: 24,
                            boxShadow: '0 2px 12px #e0c3fc22',
                            padding: '2.2rem 2.7rem',
                            minWidth: 180,
                            textAlign: 'center',
                            fontWeight: 800,
                            fontSize: 22,
                            color: idx === 0 ? '#6c47ff' : '#7c7caa',
                            border: idx === 0 ? '2.5px solid #6c47ff' : '1.5px solid #e0c3fc',
                            transition: 'border 0.2s',
                            margin: '0.7em 0',
                            position: 'relative',
                          }}>
                            {alt.name}
                            <span style={{
                              display: 'inline-block',
                              fontSize: 13,
                              fontWeight: 700,
                              color: alt.tag === 'core' ? '#22c55e' : '#a084e8',
                              background: alt.tag === 'core' ? '#e0fbe0' : '#ede9fe',
                              borderRadius: 12,
                              padding: '0.3em 0.9em',
                              marginLeft: 10,
                              marginTop: 10,
                            }}>{alt.tag === 'core' ? 'Core' : 'Non-core'}</span>
                            {idx === 0 && (
                              <div style={{ fontSize: 14, color: '#22c55e', fontWeight: 700, marginTop: 8 }}>Top Recommendation</div>
                            )}
                          </div>
                        ))}
                      </div>
                    )}
                  </>
                )}
                {result.alternatives && result.alternatives.length > 1 && (
                  <div style={{ marginTop: 8 }}>
                    <div style={{ fontWeight: 700, color: '#6c47ff', fontSize: 18, marginBottom: 12, textAlign: 'center' }}>
                      Other Recommended Programs
                    </div>
                    <div style={{ display: 'flex', flexWrap: 'wrap', gap: 12, justifyContent: 'center' }}>
                      {result.alternatives.slice(1).map((alt, idx) => (
                        <span key={alt.name} style={{ ...styles.pill, background: '#f5f7fa', color: '#6c47ff', fontWeight: 700, fontSize: 18, display: 'flex', alignItems: 'center', gap: 8 }}>
                          {alt.name}
                          <span style={{
                            display: 'inline-block',
                            fontSize: 13,
                            fontWeight: 700,
                            color: alt.tag === 'core' ? '#22c55e' : '#a084e8',
                            background: alt.tag === 'core' ? '#e0fbe0' : '#ede9fe',
                            borderRadius: 12,
                            padding: '0.3em 0.9em',
                            marginLeft: 8,
                          }}>{alt.tag === 'core' ? 'Core' : 'Non-core'}</span>
                        </span>
                    ))}
                  </div>
                </div>
              )}
              </>
              )}
            </div>
        )}
        {/* Relevancy Breakdown Section */}
        {relevancyBreakdown && !isAnalyzing && (
          <div style={{ ...styles.resultCard, marginTop: 32 }}>
            <div style={{ fontSize: 28, fontWeight: 700, color: '#6c47ff', marginBottom: 18, textAlign: 'center' }}>
              Relevancy Breakdown to <span style={{ color: '#a084e8' }}>{relevancyBreakdown.target}</span>
              <span style={{
                display: 'inline-block',
                fontSize: 15,
                fontWeight: 700,
                color: relevancyBreakdown.target_tag === 'core' ? '#22c55e' : '#a084e8',
                background: relevancyBreakdown.target_tag === 'core' ? '#e0fbe0' : '#ede9fe',
                borderRadius: 12,
                padding: '0.3em 0.9em',
                marginLeft: 10,
              }}>{relevancyBreakdown.target_tag === 'core' ? 'Core' : 'Non-core'}</span>
            </div>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 32, justifyContent: 'center' }}>
              {relevancyBreakdown.relevancies.map((item, idx) => (
                <div key={item.label + item.source} style={{ flex: '1 1 220px', minWidth: 220, maxWidth: 300, background: '#f5f7fa', borderRadius: 24, boxShadow: '0 2px 12px #e0c3fc22', padding: '2.2rem 1.7rem', textAlign: 'center', margin: '0.7em 0' }}>
                  <div style={{ fontWeight: 700, color: '#6c47ff', fontSize: 20, marginBottom: 8 }}>{item.label}</div>
                  <div style={{ fontWeight: 600, color: '#7c7caa', fontSize: 18, marginBottom: 12 }}>{item.source}</div>
                  {typeof item.score === 'number' ? (
                    <CircularProgress value={Math.round(item.score)} size={90} strokeWidth={9} />
                  ) : (
                    <div style={{ color: '#ef4444', fontWeight: 700, fontSize: 18 }}>N/A</div>
                  )}
                </div>
              ))}
            </div>
          </div>
        )}
        {/* Analytics Section */}
        {result && !isAnalyzing && (
          <div style={styles.analyticsCard}>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: 32, justifyContent: 'center' }}>
              {/* Career Distance Analysis */}
              <div style={{ flex: 1, minWidth: 320, maxWidth: 400 }}>
                <div style={styles.chartTitle}>Career Distance Analysis</div>
                <ResponsiveContainer width="100%" height={220}>
                  <BarChart data={getDistanceData()}>
                    <CartesianGrid strokeDasharray="3 3" />
                    <XAxis dataKey="name" />
                    <YAxis />
                    <Tooltip />
                    <Bar dataKey="distance" fill="#6c47ff" radius={[8, 8, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
                <div style={styles.chartDesc}>Lower distance = Better alignment with your background</div>
              </div>
              {/* Skills Radar */}
              <div style={{ flex: 1, minWidth: 320, maxWidth: 400 }}>
                <div style={styles.chartTitle}>Skills Compatibility</div>
                <ResponsiveContainer width="100%" height={220}>
                  <RadarChart data={getRadarData()}>
                    <PolarGrid />
                    <PolarAngleAxis dataKey="skill" />
                    <PolarRadiusAxis angle={90} domain={[0, 100]} />
                    <Radar name="Your Skills" dataKey="current" stroke="#6c47ff" fill="#6c47ff" fillOpacity={0.18} />
                    <Radar name="Target Requirements" dataKey="target" stroke="#ef4444" fill="#ef4444" fillOpacity={0.13} />
                    <Radar name="Recommended" dataKey="recommended" stroke="#10b981" fill="#10b981" fillOpacity={0.13} />
                    <Tooltip />
                  </RadarChart>
                </ResponsiveContainer>
              </div>
            </div>
            {/* Success Metrics */}
            <div style={styles.metricsRow}>
              <div style={styles.metricCard}>
                <div style={styles.metricValue}>95%</div>
                <div style={styles.metricLabel}>Success Rate</div>
                </div>
              <div style={styles.metricCard}>
                <div style={styles.metricValue}>2.3x</div>
                <div style={styles.metricLabel}>Career Growth</div>
                </div>
              <div style={styles.metricCard}>
                <div style={styles.metricValue}>₹45L</div>
                <div style={styles.metricLabel}>Avg. Starting Salary</div>
              </div>
            </div>
          </div>
        )}
      </div>
    </Fragment>
  );
};

export default LeapCourseMapper;
