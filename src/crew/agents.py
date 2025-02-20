from crewai import Agent, Task
from typing import List, Dict, Any
from ..core.config import settings

class MainCrew:
    """
    Main orchestrator for CrewAI agents.
    Handles agent creation and task execution.
    """
    
    def __init__(self):
        self.agents = self._create_agents()
        
    def _create_agents(self) -> List[Agent]:
        """
        Create the required AI agents.
        Override this method to customize agent configuration.
        """
        return [
            Agent(
                name="Primary Agent",
                role="Main task executor",
                goal="Execute the primary task efficiently",
                backstory="An expert agent specialized in the main task",
                allow_delegation=True,
                verbose=True,
                llm_config={
                    "model": "gpt-4",
                    "temperature": 0.7,
                    "api_key": settings.OPENAI_API_KEY
                }
            ),
            # Add more agents as needed
        ]
    
    async def execute_task(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a task using the agent crew.
        
        Args:
            input_data: Task input parameters
            
        Returns:
            Dictionary containing task results or error information
        """
        try:
            # Create tasks
            tasks = [
                Task(
                    description="Primary task execution",
                    agent=self.agents[0],
                    expected_output="Task results in specified format",
                    context=input_data
                )
            ]
            
            # Execute tasks
            results = await self.agents[0].execute(tasks[0])
            
            return {
                "status": "success",
                "results": results
            }
            
        except Exception as e:
            return {
                "status": "error",
                "error": str(e)
            } 