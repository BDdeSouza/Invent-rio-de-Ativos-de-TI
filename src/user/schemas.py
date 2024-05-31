from pydantic import BaseModel, Field
from typing import Optional


class UserPost(BaseModel):
    name: str = Field(min_lenght=2, max_lenght=200)
    cpf: str = Field(min_lenght=2, max_lenght=20)
    
    notebook: bool = Field(default=False)
    tag_nb: Optional[str] = Field(default=None)
    modelo_nb: Optional[str] = Field(default=None)
    num_serie_nb: Optional[str] = Field(default=None)
    versao_nb: Optional[str] = Field(default=None)
    configs_nb: Optional[str] = Field(default=None)
    observacao_nb: Optional[str] = Field(default=None)
    
    monitor_1: bool = Field(default=False)
    modelo_m1: Optional[str] = Field(default=None)
    num_serie_m1: Optional[str] = Field(default=None)
    observacao_m1: Optional[str] = Field(default=None)
    
    monitor_2: bool = Field(default=False)
    modelo_m2: Optional[str] = Field(default=None)
    num_serie_m2: Optional[str] = Field(default=None)
    observacao_m2: Optional[str] = Field(default=None)
    
    teclado: bool = Field(default=False)
    modelo_teclado: Optional[str] = Field(default=None)
    num_serie_teclado: Optional[str] = Field(default=None)
    observacao_teclado: Optional[str] = Field(default=None)
    
    mouse: bool = Field(default=False)
    modelo_mouse: Optional[str] = Field(default=None)
    num_serie_mouse: Optional[str] = Field(default=None)
    observacao_mouse: Optional[str] = Field(default=None)
    
    desktop: bool = Field(default=False)
    tag_desktop: Optional[str] = Field(default=None)
    modelo_desktop: Optional[str] = Field(default=None)
    num_serie_desktop: Optional[str] = Field(default=None)
    versao_desktop: Optional[str] = Field(default=None)
    configs_desktop: Optional[str] = Field(default=None)
    observacao_desktop: Optional[str] = Field(default=None)
    
    acessorios: bool = Field(default=False)
    suporte_notebook: bool = Field(default=False)
    mouse_pad: bool = Field(default=False)
    
    no_break: bool = Field(default=False)
    modelo_no: Optional[str] = Field(default=None)
    num_serie_no: Optional[str] = Field(default=None)
    
    headset: bool = Field(default=False)
    modelo_headset: Optional[str] = Field(default=None)
    num_serie_headset: Optional[str] = Field(default=None)
    
    celular: bool = Field(default=False)
    modelo_cel: Optional[str] = Field(default=None)
    imei_celular: Optional[str] = Field(default=None)
    numero_celular: Optional[str] = Field(default=None)
    observacao_celular: Optional[str] = Field(default=None)
    
    