
VENV_ACTIVATE = ~/.pyenv/versions/apicp/bin/activate
run:
	@uvicorn camp_api.main:app --reload 
create-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic revision --autogenerate 

run-migrations:
	@PYTHONPATH=$PYTHONPATH:$(pwd) alembic upgrade head 