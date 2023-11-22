import React, { useState } from "react";
import { Draggable, Droppable } from "react-beautiful-dnd";
import { generateUniqueAlphabet } from "../utils";

const Card = ({ title = {}, setData, data }) => {
  const [showMiniCard, setShowMiniCard] = useState(false);
  const [addNewField, setAddNewField] = useState("");
  const [openedInputFiledId, setOpenedInputFieldId] = useState("");

  const addNewCardItem = () => {
    if (addNewField.trim().length > 0) {
      setShowMiniCard(!showMiniCard);
      const upadtedData = data?.map((item) => {
        if (item.id === title.id) {
          return {
            ...item,
            cardList: [
              ...item.cardList,
              {
                title: addNewField,
                id: generateUniqueAlphabet(),
              },
            ],
          };
        } else {
          return item;
        }
      });
      setAddNewField("");
      setData(upadtedData);
    }
  };

  const keypress = (event) => {
    if (event.key === "Enter") {
      addNewCardItem();
    }
  };

  const deleteHandler = (id) => {
    const updatedCardList = title?.cardList?.filter(
      (cardItem) => cardItem.id !== id
    );
    if (updatedCardList) {
      const updatedData = data?.map((list) => {
        if (list.id === title?.id) {
          return {
            ...list,
            cardList: updatedCardList,
          };
        } else {
          return list;
        }
      });
      setData(updatedData);
    }
  };

  function handleConfirmClick(id) {
    const confirmed = window.confirm(
      "Are you sure you want to delete this card?"
    );
    if (confirmed) {
      deleteHandler(id);
    }
  }

  return (
    <div
      className={`bg-black flex flex-col text-white w-60 p-2 gap-4 rounded-xl `}
    >
      <input
        id={title?.id}
        type={"text"}
        value={title.title}
        onChange={(e) => {
          const upadtedData = data?.map((item) => {
            if (item.id === title.id) {
              return {
                ...item,
                title: e.target.value,
              };
            } else {
              return item;
            }
          });
          setData(upadtedData);
        }}
        className="text-lg font-semibold rounded px-2 py-1 text-white bg-black  w-full"
      />
      <Droppable droppableId={title.id}>
        {(provided, snapshot) => {
          return (
            <div
              ref={provided.innerRef}
              {...provided.droppableProps}
              className="draggable-list flex flex-col gap-4"
            >
              {title?.cardList?.map((item, key) => {
                return (
                  <Draggable key={item.id} index={key} draggableId={item.id}>
                    {(provided) => {
                      return (
                        <div
                          key={key}
                          className="w-42"
                          ref={provided.innerRef}
                          {...provided.draggableProps}
                          {...provided.dragHandleProps}
                        >
                          {openedInputFiledId === item.id && (
                            <input
                              key={item?.id}
                              className="text-sm font-semibold rounded p-2 text-white outline-none bg-[#22272B] !w-full flex justify-between"
                              value={item?.title}
                              type={"text"}
                              onKeyDown={(e) => {
                                if (e.key === "Enter") {
                                  setOpenedInputFieldId("");
                                }
                              }}
                              onChange={(e) => {
                                const updatedCardList = title?.cardList?.map(
                                  (cardItem) => {
                                    if (cardItem.id === item.id) {
                                      return {
                                        ...cardItem,
                                        title: e.target.value,
                                      };
                                    }
                                    return cardItem;
                                  }
                                );
                                if (updatedCardList) {
                                  const updatedData = data?.map((list) => {
                                    if (list.id === title?.id) {
                                      return {
                                        ...list,
                                        cardList: updatedCardList,
                                      };
                                    } else {
                                      return list;
                                    }
                                  });
                                  setData(updatedData);
                                }
                              }}
                            />
                          )}
                          {openedInputFiledId !== item?.id && (
                            <div
                              key={item?.id}
                              className="text-sm font-semibold rounded p-2 text-white outline-none bg-[#22272B] !w-full flex justify-between items-center"
                            >
                              <div className="w-[160px] h-auto break-all	">
                                {item?.title}
                              </div>
                              <div className="flex gap-2">
                                <div
                                  className="cursor-pointer"
                                  onClick={() => {
                                    if (openedInputFiledId.length === 0)
                                      setOpenedInputFieldId(item?.id);
                                  }}
                                >
                                  <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    strokeWidth={1.5}
                                    stroke="currentColor"
                                    className="w-4 h-4"
                                  >
                                    <path
                                      strokeLinecap="round"
                                      strokeLinejoin="round"
                                      d="M16.862 4.487l1.687-1.688a1.875 1.875 0 112.652 2.652L6.832 19.82a4.5 4.5 0 01-1.897 1.13l-2.685.8.8-2.685a4.5 4.5 0 011.13-1.897L16.863 4.487zm0 0L19.5 7.125"
                                    />
                                  </svg>
                                </div>
                                <div
                                  className="cursor-pointer"
                                  onClick={() => handleConfirmClick(item.id)}
                                >
                                  <svg
                                    xmlns="http://www.w3.org/2000/svg"
                                    fill="none"
                                    viewBox="0 0 24 24"
                                    strokeWidth={1.5}
                                    stroke="currentColor"
                                    className="w-4 h-4"
                                  >
                                    <path
                                      strokeLinecap="round"
                                      strokeLinejoin="round"
                                      d="M14.74 9l-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 01-2.244 2.077H8.084a2.25 2.25 0 01-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 00-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 013.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 00-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 00-7.5 0"
                                    />
                                  </svg>
                                </div>
                              </div>
                            </div>
                          )}
                        </div>
                      );
                    }}
                  </Draggable>
                );
              })}
              {provided.placeholder}
            </div>
          );
        }}
      </Droppable>
      {!showMiniCard && (
        <button
          className="text-sm p-1 rounded-lg font-semibold hover:bg-[#84B8FE] flex justify-start items-center"
          onClick={() => setShowMiniCard(!showMiniCard)}
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
            strokeWidth={1.5}
            stroke="currentColor"
            className="w-6 h-6"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              d="M12 6v12m6-6H6"
            />
          </svg>
          Add a card
        </button>
      )}
      {showMiniCard && (
        <div className="bg-black flex flex-col gap-4">
          <input
            id={"miniCard"}
            type={"text"}
            value={addNewField}
            onChange={(e) => {
              setAddNewField(e.target.value);
            }}
            className="text-sm w-42 font-semibold rounded p-2 text-white outline-none bg-[#22272B]"
            autoFocus
            placeholder="Enter a title for this card..."
            onKeyDown={keypress}
          />
          <div className="flex gap-2 items-center">
            <button
              className="bg-[#84B8FE] w-20 p-1 rounded-lg text-sm font-semibold"
              onClick={() => {
                addNewCardItem();
              }}
            >
              Add Card
            </button>
            <div
              className="cursor-pointer"
              onClick={() => {
                setShowMiniCard(!showMiniCard);
                setAddNewField("");
              }}
            >
              <svg
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                strokeWidth={1.5}
                stroke="currentColor"
                className="w-6 h-6"
              >
                <path
                  strokeLinecap="round"
                  strokeLinejoin="round"
                  d="M6 18L18 6M6 6l12 12"
                />
              </svg>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

export default Card;
