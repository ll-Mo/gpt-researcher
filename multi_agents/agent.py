from multi_agents.agents import ChiefEditorAgent

chief_editor = ChiefEditorAgent({
  "query":"Identify publicly available datasets and resources used for training large language models (LLMs) on content moderation, specifically focusing on categories like illegal content, child abuse, hate speech, violence, harassment, malware, misinformation, and harmful content. Include information about dataset size, annotation methodology, and any ethical considerations.",
  "max_sections": 3,
  "follow_guidelines": False,
  "model": "gpt-4o",
  "guidelines": [
    "The report MUST be written in APA format",
    "Each section must discuss at least one specific dataset or resource used in LLM training for content moderation, providing its name and a brief description.",
    "For each dataset/resource, specify its annotation methodology (e.g., human-annotated, synthetically generated), and a direct link to its documentation or repository.",
    "At least two sections should compare and contrast different datasets/resources based on annotation methodology, and suitability for LLM training in content moderation.  Use a table format for clarity.",
    "Include a concluding section summarizing the key findings and suggesting potential areas for future research in LLM dataset development for content moderation."
  ],
  "verbose": False
}, websocket=None, stream_output=True)
graph = chief_editor.init_research_team()
graph = graph.compile()