from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.task_repository import TaskRespository
from app.services.task_service import TaskService
from app.models.task import Task
from app.schemas.task import TaskCreated, TaskResponse, TaskUpdated
from app.dependencies import get_db_session
from app.security.jwt_dependency import current_user
from app.security.role_dependency import require_roles


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
        
@router.get('/getAllTasks', response_model=List[TaskResponse])
def get_all_tasks(db:Session=Depends(get_db_session),
                  current_user:dict=Depends(current_user),
                  user=Depends(require_roles("superadmin"))) -> List[TaskResponse]:
    try:
        response=_service.get_all_task(db)
        
        if not response:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='there arent tasks inot the bd'
            )
            
        return response
    
    except HTTPException as e:
        raise HTTPException(
                status_code=status.WS_1014_BAD_GATEWAY,
                detail=f'there arent tasks inot the bd {e}'
            )
        
@router.get('/getMyTasks', response_model=List[TaskResponse])
def get_my_tasks(db:Session=Depends(get_db_session),
                 current_user:dict=Depends(current_user)) -> List[TaskResponse]:
    try:
        response=_service.get_all_my_task(db,current_user['user_id'])
        
        if not response:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='you dont have task created yet'
            )
            
        return response
        
        
    except HTTPException as e:
        raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f'there arent tasks inot the bd {e}'
            )
        
@router.delete('/deleteTaskById/:id')
def delete_task(id:int,
                db:Session=Depends(get_db_session),
                current_user:dict=Depends(current_user)):
    try:
        
        response=_service.delete_task(db, id)
        
        if response:
            return {'message':'task deleted correctly'}
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='we cant delete the task'
        )
        
        
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'we cant delete the task {e}'
        )
        
@router.put('/updateTask/:taskId', response_model=TaskResponse)
def updated_task_by_id(taskId:int,
                       data:TaskUpdated,
                       db:Session=Depends(get_db_session),
                       current_user:dict=Depends(current_user)) -> TaskResponse:
    try:
        response=_service.update_task(db, data, taskId)
        
        if not response:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='there was happened an error'
            )
            
        return response
    
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'there was happened an error {e}'
        )
        
        
