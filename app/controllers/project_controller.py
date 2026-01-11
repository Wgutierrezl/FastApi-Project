from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.dependencies import get_db_session
from app.security.jwt_dependency import current_user
from app.repositories.project_repository import ProjectRepository
from app.services.project_service import ProjectService
from app.schemas.project import ProjectResponse, projectCreated

_service=ProjectService(projectRepository=ProjectRepository())

router=APIRouter(prefix='/projects',
                 tags=['/Projects'],
                 dependencies=[Depends(current_user)])

@router.post('/createProject')
def create_project(data:projectCreated,
                   db:Session=Depends(get_db_session), 
                   current_user:dict=Depends(current_user)) -> ProjectResponse:
    try:
        response=_service.create_project(db, data, current_user['user_id'])
        
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='we dont create the project'
            )
            
        return response
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"error {e}"
        )
        
@router.get('/getProjectsByUserId/:userId', response_model=List[ProjectResponse])
def get_projects_by_userid(userId:str,
                       db:Session=Depends(get_db_session),
                       current_user:dict=Depends(current_user)):
    try:
        response=_service.get_projects_by_user_id(db, userId)
        
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='el usuario aun no tiene projectos'
            )
        
        return response
    
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"there was an error {e}"
        )
        
@router.get('/getMyProjects', response_model=List[ProjectResponse])
def get_my_projects(db:Session=Depends(get_db_session),
                    current_user:dict=Depends(current_user)):
    try:
        response=_service.get_projects_by_user_id(db, current_user['user_id'])
        
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='you dont have projects yet'
            )
        
        return response
    
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"there was an error {e}"
        )

@router.get('/getAllProjects', response_model=List[ProjectResponse])    
def get_all_projects(db:Session=Depends(get_db_session),
                     current_user:dict=Depends(current_user)) -> List[ProjectResponse]:
    try:
        response=_service.get_all_projects(db)
        
        if response is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='there´s no projects in the db'
            )
            
        return response
    
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"there was happened an error {e}"
        )
        
@router.delete('/deleteProjectById/:id')
def delete_project(id:int,
                   db:Session=Depends(get_db_session),
                   current_user:dict=Depends(current_user)):
    try:
        response=_service.delete_project(db, id)
        
        if response:
            return {'message':'project deleted'}
        
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='we cant delete the project'
        ) 
        
    except HTTPException as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'we cant delete the project {e}'
        ) 
        