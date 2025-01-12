from graphviz import Digraph

# Create a directed graph for the architecture
diagram = Digraph("Quant-AI-Sage_Architecture", format="png")
diagram.attr(rankdir="TB", size="8,10")

# Data Ingestion Layer
diagram.node("Data Ingestion Layer", "Data Ingestion Layer\n(REST API, Preprocessing)", shape="box", style="rounded,filled", color="lightblue")

# Data Storage Layer
diagram.node("Data Storage Layer", "Data Storage Layer\n(SQLite/PostgreSQL)", shape="cylinder", style="filled", color="lightgray")

# Technical Analysis Module
diagram.node("Technical Analysis Module", "Technical Analysis Module\n(Indicators, Scheduling)", shape="box", style="rounded,filled", color="orange")

# Prediction Engine
diagram.node("Prediction Engine", "Prediction Engine\n(LLM Wrapper, Feature Extraction)", shape="box", style="rounded,filled", color="yellow")

# Trading Module
diagram.node("Trading Module", "Trading Module\n(Order Management, Risk Management)", shape="box", style="rounded,filled", color="green")

# Message Bus
diagram.node("Message Bus", "Message Bus\n(Pub/Sub, Decoupling)", shape="ellipse", style="dotted", color="black")

# Connect components
diagram.edges([
    ("Data Ingestion Layer", "Data Storage Layer"),  # Data stored in DB
    ("Data Ingestion Layer", "Message Bus"),         # Real-time data to Message Bus
    ("Data Storage Layer", "Technical Analysis Module"),  # Analysis uses historical data
    ("Technical Analysis Module", "Data Storage Layer"),  # Save analysis results
    ("Technical Analysis Module", "Message Bus"),         # Forward indicators to Message Bus
    ("Message Bus", "Prediction Engine"),                 # Message Bus to Prediction Engine
    ("Data Storage Layer", "Prediction Engine"),          # Prediction Engine uses stored data
    ("Prediction Engine", "Message Bus"),                 # Forward predictions to Message Bus
    ("Message Bus", "Trading Module"),                    # Forward predictions to Trading Module
    ("Prediction Engine", "Trading Module")               # Direct prediction flow (if Message Bus bypassed)
])

# Render the diagram
diagram_path = "Quant_AI_Sage_Architecture"
diagram.render(diagram_path, format="png", cleanup=True)
diagram_path + ".png"
