from aiogram import F,Router
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State,StatesGroup
from aiogram.filters import StateFilter


user_dict: dict[int , dict[str, str|int|bool]] = {}

class FSMFillForm(StatesGroup):
    fill_name = State()
    fill_age = State()
    fill_phone = State()
router = Router()


@router.callback_query(F.data == "document1")
async def doc1(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.answer('Введите ваше ФИО:')
    await state.set_state(FSMFillForm.fill_name)

@router.message(StateFilter(FSMFillForm.fill_name))
async def fio(message: types.Message,state:FSMContext):
    await state.update_data(fio=message.text)
    await message.answer(f"Возраст:")
    await state.set_state(FSMFillForm.fill_age)

@router.message(StateFilter(FSMFillForm.fill_age))
async def fio(message: types.Message,state:FSMContext):
    await state.update_data(age=message.text)
    await message.answer(f"Телефон:")
    await state.set_state(FSMFillForm.fill_phone)

@router.message(StateFilter(FSMFillForm.fill_phone))
async def age(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await message.answer("Спасибо")
    user_id = message.from_user.id
    user_data = await state.get_data()


    #что то надо сделать с этими данными кароч

    await state.clear()