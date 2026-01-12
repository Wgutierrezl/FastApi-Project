from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.task_repository import TaskRespository
from app.services.task_service import TaskService
from app.models.task import Task
from app.schemas.task import TaskCreated, TaskResponse, TaskUpdated
from app.dependencies import get_db_session
from app.security.jwt_dependency import current_user


router=APIRouter(prefix='/tasks',
                 tags=['Tasks'],
                 dependencies=[Depends(current_user)])

_service=TaskService(repo=TaskRespository())


@router.post('/createTask', response_model=TaskResponse)
def create_Task(data:TaskCreated,
                db:Session=Depends(get_db_session),
                current_user:dict=Depends(current_user)) -> TaskResponse:
    try:
        
        response=_service.create_task(db, data, current_user['user_id'])
        
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='we cant create the task'
            )
            
        return response
    
    except HTTPException as ex:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"there was happeneed and error {ex}"
        )
