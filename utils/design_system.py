"""
Professional Design System for Telco Network Optimization Suite
Provides consistent styling, components, and utilities across all pages.
"""

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from datetime import datetime
import time

# =============================================================================
# DESIGN TOKENS
# =============================================================================

class Colors:
    """Professional color palette for the application"""
    # Primary brand colors
    PRIMARY = "#1f4e79"          # Deep professional blue
    PRIMARY_LIGHT = "#2d6ba0"    # Lighter blue for highlights
    PRIMARY_DARK = "#163d61"     # Darker blue for emphasis
    
    # Secondary colors
    SECONDARY = "#28a745"        # Success green
    WARNING = "#ffc107"          # Warning yellow
    DANGER = "#dc3545"           # Error red
    INFO = "#17a2b8"            # Info teal
    
    # Neutral colors
    WHITE = "#ffffff"
    LIGHT_GRAY = "#f8f9fa"
    MEDIUM_GRAY = "#6c757d"
    DARK_GRAY = "#343a40"
    BLACK = "#000000"
    
    # Status colors
    SUCCESS = "#28a745"
    ERROR = "#dc3545"
    NEUTRAL = "#6c757d"
    
    # Chart colors (professional palette)
    CHART_COLORS = [
        "#1f4e79", "#28a745", "#ffc107", "#dc3545", "#17a2b8",
        "#6f42c1", "#fd7e14", "#20c997", "#e83e8c", "#6c757d"
    ]

class Typography:
    """Typography system for consistent text styling"""
    H1_SIZE = "2.5rem"
    H2_SIZE = "2rem" 
    H3_SIZE = "1.5rem"
    H4_SIZE = "1.25rem"
    BODY_SIZE = "1rem"
    SMALL_SIZE = "0.875rem"
    
class Spacing:
    """Spacing system for consistent layouts"""
    XS = "0.25rem"
    SM = "0.5rem" 
    MD = "1rem"
    LG = "1.5rem"
    XL = "2rem"
    XXL = "3rem"

# =============================================================================
# CUSTOM CSS
# =============================================================================

def inject_custom_css():
    """Inject professional custom CSS into the Streamlit app"""
    st.markdown("""
    <style>
    /* Import professional fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Main app styling */
    .main > div {
        padding-top: 2rem;
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Professional header styling */
    .app-header {
        background: linear-gradient(135deg, #1f4e79 0%, #2d6ba0 100%);
        color: white;
        padding: 2rem;
        border-radius: 12px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(31, 78, 121, 0.2);
    }
    
    .app-header h1 {
        margin: 0;
        font-weight: 600;
        font-size: 2.5rem;
        line-height: 1.2;
    }
    
    .app-header p {
        margin: 0.5rem 0 0 0;
        opacity: 0.9;
        font-size: 1.1rem;
        font-weight: 300;
    }
    
    /* Professional metric cards */
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        border-left: 4px solid #1f4e79;
        margin-bottom: 1rem;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.12);
    }
    
    .metric-card h3 {
        color: #1f4e79;
        margin: 0 0 0.5rem 0;
        font-size: 1.25rem;
        font-weight: 600;
    }
    
    .metric-card .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2d6ba0;
        margin: 0;
        line-height: 1;
    }
    
    .metric-card .metric-delta {
        font-size: 0.875rem;
        margin-top: 0.5rem;
        font-weight: 500;
    }
    
    /* Professional info boxes */
    .info-box {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem 1.25rem;
        margin: 1rem 0;
        font-weight: 500;
    }
    
    .info-box.success {
        background: #d4edda;
        border-color: #c3e6cb;
        color: #155724;
    }
    
    .info-box.warning {
        background: #fff3cd;
        border-color: #ffeaa7;
        color: #856404;
    }
    
    .info-box.error {
        background: #f8d7da;
        border-color: #f1aeb5;
        color: #721c24;
    }
    
    /* Loading spinner */
    .loading-spinner {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 4rem 2rem;
        text-align: center;
    }
    
    /* Professional buttons */
    .stButton > button {
        background: linear-gradient(135deg, #1f4e79 0%, #2d6ba0 100%);
        color: white;
        border-radius: 8px;
        border: none;
        padding: 0.75rem 1.5rem;
        font-weight: 600;
        font-family: 'Inter', sans-serif;
        transition: all 0.3s ease;
        box-shadow: 0 2px 8px rgba(31, 78, 121, 0.2);
    }
    
    .stButton > button:hover {
        background: linear-gradient(135deg, #163d61 0%, #1f4e79 100%);
        transform: translateY(-1px);
        box-shadow: 0 4px 16px rgba(31, 78, 121, 0.3);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
        border-right: 1px solid #e9ecef;
    }
    
    /* Chart containers */
    .chart-container {
        background: white;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
        margin-bottom: 1.5rem;
    }
    
    /* Data tables */
    .dataframe {
        border-radius: 8px;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
        font-family: 'Inter', sans-serif;
    }
    
    /* Status indicators */
    .status-indicator {
        display: inline-block;
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 8px;
    }
    
    .status-success { background-color: #28a745; }
    .status-warning { background-color: #ffc107; }
    .status-error { background-color: #dc3545; }
    .status-neutral { background-color: #6c757d; }
    
    /* Professional section headers */
    .section-header {
        background: linear-gradient(90deg, #f8f9fa 0%, transparent 100%);
        padding: 1rem 0;
        border-left: 4px solid #1f4e79;
        padding-left: 1rem;
        margin: 2rem 0 1rem 0;
    }
    
    .section-header h3 {
        margin: 0;
        color: #1f4e79;
        font-weight: 600;
    }
    
    /* Responsive improvements */
    @media (max-width: 768px) {
        .app-header {
            padding: 1.5rem;
        }
        
        .app-header h1 {
            font-size: 2rem;
        }
        
        .metric-card .metric-value {
            font-size: 2rem;
        }
    }
    
    </style>
    """, unsafe_allow_html=True)

# =============================================================================
# COMMON COMPONENTS
# =============================================================================

def create_page_header(title: str, description: str, icon: str = "📊"):
    """Create a professional page header with consistent styling"""
    st.markdown(f"""
    <div class="app-header">
        <h1>{icon} {title}</h1>
        <p>{description}</p>
    </div>
    """, unsafe_allow_html=True)

def create_metric_card(title: str, value: str, delta: str = None, delta_color: str = "normal"):
    """Create a professional metric card"""
    delta_html = ""
    if delta:
        color_style = {
            "normal": "color: #6c757d;",
            "positive": "color: #28a745;",
            "negative": "color: #dc3545;"
        }.get(delta_color, "color: #6c757d;")
        delta_html = f"<div class='metric-delta' style='{color_style}'>{delta}</div>"
    
    st.markdown(f"""
    <div class="metric-card">
        <h3>{title}</h3>
        <div class="metric-value">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def create_info_box(message: str, box_type: str = "info"):
    """Create professional info/alert boxes"""
    icons = {
        "info": "ℹ️",
        "success": "✅", 
        "warning": "⚠️",
        "error": "❌"
    }
    
    icon = icons.get(box_type, "ℹ️")
    st.markdown(f"""
    <div class="info-box {box_type}">
        {icon} {message}
    </div>
    """, unsafe_allow_html=True)

def show_loading_state(message: str = "Loading data..."):
    """Show a professional loading state"""
    return st.markdown(f"""
    <div class="loading-spinner">
        <div>
            <div style="font-size: 3rem; margin-bottom: 1rem;">⏳</div>
            <div style="color: #6c757d; font-size: 1.1rem; font-weight: 500;">{message}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_status_indicator(status: str, text: str = None):
    """Create status indicators with colors"""
    status_classes = {
        "success": "status-success",
        "warning": "status-warning", 
        "error": "status-error",
        "neutral": "status-neutral"
    }
    
    class_name = status_classes.get(status.lower(), "status-neutral")
    display_text = text or status.title()
    
    st.markdown(f"""
    <span class="status-indicator {class_name}"></span>{display_text}
    """, unsafe_allow_html=True)

def create_section_header(title: str, icon: str = ""):
    """Create professional section headers"""
    st.markdown(f"""
    <div class="section-header">
        <h3>{icon} {title}</h3>
    </div>
    """, unsafe_allow_html=True)

# =============================================================================
# CHART STYLING
# =============================================================================

def get_professional_chart_layout():
    """Get professional layout settings for Plotly charts"""
    return {
        'plot_bgcolor': 'white',
        'paper_bgcolor': 'white',
        'font': {
            'family': 'Inter, Arial, sans-serif',
            'size': 12,
            'color': Colors.DARK_GRAY
        },
        'title': {
            'font': {'size': 18, 'color': Colors.PRIMARY, 'family': 'Inter'},
            'x': 0.5,
            'xanchor': 'center',
            'pad': {'t': 20}
        },
        'xaxis': {
            'gridcolor': '#f0f0f0',
            'linecolor': '#e0e0e0',
            'tickcolor': '#e0e0e0',
            'title_font': {'size': 14, 'color': Colors.DARK_GRAY}
        },
        'yaxis': {
            'gridcolor': '#f0f0f0', 
            'linecolor': '#e0e0e0',
            'tickcolor': '#e0e0e0',
            'title_font': {'size': 14, 'color': Colors.DARK_GRAY}
        },
        'legend': {
            'bgcolor': 'rgba(255,255,255,0.9)',
            'bordercolor': '#e0e0e0',
            'borderwidth': 1,
            'font': {'size': 11}
        },
        'margin': {'t': 60, 'b': 60, 'l': 60, 'r': 60}
    }

def style_plotly_chart(fig):
    """Apply professional styling to Plotly charts"""
    fig.update_layout(**get_professional_chart_layout())
    return fig

def create_professional_metric_charts(data: pd.DataFrame, x_col: str, y_col: str, chart_type: str = "bar", title: str = ""):
    """Create professionally styled charts"""
    
    if chart_type == "bar":
        fig = px.bar(data, x=x_col, y=y_col, title=title,
                     color_discrete_sequence=Colors.CHART_COLORS)
    elif chart_type == "line":
        fig = px.line(data, x=x_col, y=y_col, title=title,
                      color_discrete_sequence=Colors.CHART_COLORS)
        fig.update_traces(line=dict(width=3))
    elif chart_type == "scatter":
        fig = px.scatter(data, x=x_col, y=y_col, title=title,
                         color_discrete_sequence=Colors.CHART_COLORS)
        fig.update_traces(marker=dict(size=8))
    else:
        fig = px.bar(data, x=x_col, y=y_col, title=title,
                     color_discrete_sequence=Colors.CHART_COLORS)
    
    return style_plotly_chart(fig)

# =============================================================================
# SESSION MANAGEMENT
# =============================================================================

@st.cache_resource
def get_snowflake_session():
    """Get Snowflake session with proper error handling"""
    try:
        import snowflake.snowpark.context
        return snowflake.snowpark.context.get_active_session()
    except Exception as e:
        create_info_box(f"Failed to connect to Snowflake: {str(e)}", "error")
        st.stop()

def execute_query_with_loading(query: str, description: str = "Loading data..."):
    """Execute Snowflake query with professional loading state"""
    session = get_snowflake_session()
    
    # Show loading state
    loading_placeholder = st.empty()
    with loading_placeholder.container():
        show_loading_state(description)
    
    try:
        # Execute query
        result = session.sql(query).to_pandas()
        loading_placeholder.empty()
        return result
    except Exception as e:
        loading_placeholder.empty()
        create_info_box(f"Error executing query: {str(e)}", "error")
        return pd.DataFrame()

# =============================================================================
# PAGE LAYOUT HELPERS
# =============================================================================

def create_metric_grid(metrics: list, columns: int = 3):
    """Create a responsive grid layout for metrics"""
    cols = st.columns(columns)
    for i, metric in enumerate(metrics):
        with cols[i % columns]:
            create_metric_card(**metric)

def create_sidebar_navigation():
    """Create professional sidebar navigation"""
    st.sidebar.markdown("""
    <div style="text-align: center; padding: 1.5rem; background: linear-gradient(135deg, #1f4e79 0%, #2d6ba0 100%); border-radius: 12px; margin-bottom: 1.5rem;">
        <h3 style="color: white; margin: 0; font-weight: 600;">📡 Telco Network</h3>
        <p style="color: rgba(255,255,255,0.9); margin: 0.5rem 0 0 0; font-size: 0.9rem;">Optimization Suite</p>
    </div>
    """, unsafe_allow_html=True)

def add_page_footer():
    """Add professional page footer"""
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #6c757d; font-size: 0.875rem; padding: 2rem 0 1rem 0;">
        <p style="margin: 0;">🤖 Powered by <strong>Snowflake Cortex AISQL</strong> | Built with <strong>Streamlit</strong></p>
        <p style="margin: 0.5rem 0 0 0;">© 2024 AI-Enhanced Telco Network Optimization Suite</p>
    </div>
    """, unsafe_allow_html=True)


# =================== AI-SPECIFIC DESIGN COMPONENTS ===================

def create_ai_chat_interface():
    """Create AI chat interface component"""
    st.markdown("""
    <style>
    .ai-chat-container {
        background: linear-gradient(135deg, #f8f9fa 0%, #e3f2fd 100%);
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
        border: 1px solid #e3f2fd;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
    }
    .ai-chat-header {
        display: flex;
        align-items: center;
        margin-bottom: 1rem;
        color: #1565c0;
        font-weight: 600;
    }
    .ai-response-box {
        background: white;
        border-radius: 12px;
        padding: 1.5rem;
        margin-top: 1rem;
        border-left: 4px solid #4caf50;
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    }
    .ai-thinking {
        display: flex;
        align-items: center;
        color: #666;
        font-style: italic;
    }
    .ai-thinking::before {
        content: "🤖";
        margin-right: 8px;
        animation: thinking 2s infinite;
    }
    @keyframes thinking {
        0%, 50% { opacity: 1; }
        25%, 75% { opacity: 0.5; }
    }
    </style>
    """, unsafe_allow_html=True)

def create_ai_insights_card(title: str, insight: str, confidence: float = 0.0, icon: str = "🧠") -> None:
    """
    Create AI insights card with confidence indicator
    
    Args:
        title: Card title
        insight: AI-generated insight
        confidence: Confidence score (0-1)
        icon: Icon to display
    """
    confidence_color = "#4caf50" if confidence > 0.8 else "#ff9800" if confidence > 0.6 else "#f44336"
    confidence_text = "High" if confidence > 0.8 else "Medium" if confidence > 0.6 else "Low"
    
    st.markdown(f"""
    <div style="background: white; border-radius: 16px; padding: 1.5rem; margin: 1rem 0; 
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-left: 4px solid #2196f3;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <div style="display: flex; align-items: center;">
                <span style="font-size: 1.5rem; margin-right: 0.75rem;">{icon}</span>
                <h4 style="margin: 0; color: #1565c0; font-weight: 600;">{title}</h4>
            </div>
            <div style="background: {confidence_color}; color: white; padding: 0.25rem 0.75rem; 
                        border-radius: 20px; font-size: 0.8rem; font-weight: 500;">
                {confidence_text} Confidence
            </div>
        </div>
        <div style="color: #333; line-height: 1.6; font-size: 1rem;">{insight}</div>
    </div>
    """, unsafe_allow_html=True)

def create_ai_loading_spinner(message: str = "AI is analyzing...") -> None:
    """
    Create AI-themed loading spinner
    
    Args:
        message: Loading message to display
    """
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; color: #1565c0;">
        <div style="font-size: 2rem; margin-bottom: 1rem;">
            <span style="animation: spin 2s linear infinite;">🤖</span>
            <span style="animation: pulse 1s ease-in-out infinite;">🧠</span>
            <span style="animation: spin 2s linear infinite reverse;">⚡</span>
        </div>
        <div style="font-weight: 500; color: #666;">{message}</div>
    </div>
    <style>
    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    @keyframes pulse {{
        0%, 100% {{ opacity: 1; }}
        50% {{ opacity: 0.5; }}
    }}
    </style>
    """, unsafe_allow_html=True)

def create_ai_recommendation_list(recommendations: list, title: str = "AI Recommendations") -> None:
    """
    Create formatted list of AI recommendations
    
    Args:
        recommendations: List of recommendation strings
        title: Title for the recommendations section
    """
    if not recommendations:
        return
        
    recommendations_html = ""
    for i, rec in enumerate(recommendations, 1):
        recommendations_html += f"""
        <div style="background: #f8f9fa; border-left: 4px solid #4caf50; padding: 1rem; 
                    margin: 0.5rem 0; border-radius: 0 8px 8px 0;">
            <div style="display: flex; align-items: flex-start;">
                <div style="background: #4caf50; color: white; border-radius: 50%; 
                           width: 24px; height: 24px; display: flex; align-items: center; 
                           justify-content: center; font-size: 0.8rem; font-weight: bold; 
                           margin-right: 1rem; flex-shrink: 0;">{i}</div>
                <div style="flex: 1; color: #333; line-height: 1.5;">{rec}</div>
            </div>
        </div>
        """
    
    st.markdown(f"""
    <div style="background: white; border-radius: 16px; padding: 1.5rem; margin: 1rem 0; 
                box-shadow: 0 4px 20px rgba(0,0,0,0.08);">
        <h4 style="color: #1565c0; margin: 0 0 1rem 0; display: flex; align-items: center;">
            <span style="margin-right: 0.5rem;">💡</span> {title}
        </h4>
        {recommendations_html}
    </div>
    """, unsafe_allow_html=True)

def create_ai_metrics_dashboard(metrics: dict) -> None:
    """
    Create AI metrics dashboard
    
    Args:
        metrics: Dictionary of metric name -> value pairs
    """
    if not metrics:
        return
        
    cols = st.columns(min(4, len(metrics)))
    
    icons = ["🎯", "📊", "⚡", "🚀", "🔍", "💡", "🎪", "🌟"]
    
    for i, (metric, value) in enumerate(metrics.items()):
        with cols[i % len(cols)]:
            icon = icons[i % len(icons)]
            st.markdown(f"""
            <div style="background: linear-gradient(135deg, #2196f3 0%, #1976d2 100%); 
                        color: white; border-radius: 16px; padding: 1.5rem; text-align: center; 
                        box-shadow: 0 4px 20px rgba(33,150,243,0.3); margin-bottom: 1rem;">
                <div style="font-size: 2rem; margin-bottom: 0.5rem;">{icon}</div>
                <div style="font-size: 1.5rem; font-weight: bold; margin-bottom: 0.25rem;">{value}</div>
                <div style="font-size: 0.9rem; opacity: 0.9;">{metric}</div>
            </div>
            """, unsafe_allow_html=True)

def create_ai_progress_tracker(current_step: int, total_steps: int, step_name: str) -> None:
    """
    Create AI process progress tracker
    
    Args:
        current_step: Current step number (1-based)
        total_steps: Total number of steps
        step_name: Name of current step
    """
    progress = (current_step - 1) / total_steps
    
    st.markdown(f"""
    <div style="background: white; border-radius: 12px; padding: 1.5rem; margin: 1rem 0; 
                box-shadow: 0 2px 10px rgba(0,0,0,0.05); border-left: 4px solid #4caf50;">
        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
            <h4 style="margin: 0; color: #1565c0;">🤖 AI Processing Status</h4>
            <span style="color: #666; font-size: 0.9rem;">Step {current_step} of {total_steps}</span>
        </div>
        <div style="background: #e0e0e0; border-radius: 10px; height: 8px; margin-bottom: 1rem;">
            <div style="background: linear-gradient(90deg, #4caf50 0%, #66bb6a 100%); 
                        height: 100%; border-radius: 10px; width: {progress*100}%; 
                        transition: width 0.5s ease;"></div>
        </div>
        <div style="color: #666; font-size: 0.95rem;">
            <span style="margin-right: 0.5rem;">⚡</span>{step_name}
        </div>
    </div>
    """, unsafe_allow_html=True)

def create_model_selector(models: list, default_model: str = "mistral-large") -> str:
    """
    Create AI model selector component
    
    Args:
        models: List of available AI models
        default_model: Default model to select
        
    Returns:
        Selected model name
    """
    st.markdown("### 🤖 AI Model Configuration")
    
    model_descriptions = {
        "mistral-large": "🏆 Mistral Large - Best overall performance, latest capabilities",
        "mistral-7b": "⚡ Mistral 7B - Fast responses, good for simple tasks",
        "mixtral-8x7b": "🎯 Mixtral 8x7B - Balanced performance and speed",
        "llama3.1-8b": "🦙 Llama 3.1 8B - Meta's efficient model",
        "llama3.1-70b": "🦙 Llama 3.1 70B - Meta's powerful model",
        "llama3.1-405b": "🦙 Llama 3.1 405B - Meta's largest model",
        "snowflake-arctic": "❄️ Snowflake Arctic - Optimized for enterprise",
        "reka-core": "🧠 Reka Core - Advanced reasoning",
        "reka-flash": "⚡ Reka Flash - Speed optimized"
    }
    
    # Create selection with descriptions
    options = []
    for model in models:
        description = model_descriptions.get(model, f"🤖 {model}")
        options.append(f"{description}")
    
    selected_option = st.selectbox(
        "Choose AI Model:",
        options,
        index=models.index(default_model) if default_model in models else 0,
        help="Different models have different strengths. Larger models are more capable but slower."
    )
    
    # Extract model name from selection
    selected_model = models[options.index(selected_option)]
    
    # Show model info
    if selected_model in model_descriptions:
        st.info(f"Selected: {model_descriptions[selected_model]}")
    
    return selected_model

def format_ai_response(response: str, title: str = "AI Insights") -> None:
    """
    Format and display AI response in Streamlit
    
    Args:
        response: AI generated response
        title: Title for the response section
    """
    if response:
        st.markdown(f"### 🤖 {title}")
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f8f9fa 0%, #e3f2fd 100%); 
                    padding: 1.5rem; border-radius: 12px; margin: 1rem 0; 
                    border-left: 4px solid #2196f3; box-shadow: 0 2px 10px rgba(0,0,0,0.05);">
            <div style="color: #1565c0; line-height: 1.6;">{response}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning(f"No {title.lower()} available at this time.")

def create_ai_metric_card(title: str, value: str, description: str = "", icon: str = "🤖") -> None:
    """
    Create AI-specific metric card
    
    Args:
        title: Card title
        value: Main value to display
        description: Additional description
        icon: Icon to display
    """
    st.markdown(f"""
    <div style="background: white; padding: 1.5rem; border-radius: 12px; 
                box-shadow: 0 4px 20px rgba(0,0,0,0.08); border-left: 4px solid #4caf50; margin-bottom: 1rem;">
        <div style="display: flex; align-items: center; margin-bottom: 0.5rem;">
            <span style="font-size: 1.5rem; margin-right: 0.5rem;">{icon}</span>
            <h4 style="margin: 0; color: #2e7d32; font-weight: 600;">{title}</h4>
        </div>
        <div style="font-size: 1.25rem; font-weight: 500; color: #1565c0; margin-bottom: 0.5rem;">{value}</div>
        {f'<div style="color: #6c757d; font-size: 0.9rem;">{description}</div>' if description else ''}
    </div>
    """, unsafe_allow_html=True)