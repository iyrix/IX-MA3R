import { useState } from "react";
import { Header, Card } from "./components";
import { generateUniqueAlphabet } from "./utils";
import { DragDropContext } from "react-beautiful-dnd";

const App = () => {
  const [list, setList] = useState([]);
  const [data, setData] = useState([]);
  const [showMiniCard, setShowMiniCard] = useState(false);
  const [title, setTitle] = useState("");

  const handleDragEnd = (result) => {
    if (result.destination) {
      const { source, destination } = result;
      console.log("source, destination : ", source, destination);

      // Update the card list based on the drag and drop operation
      if (
        source.droppableId === destination.droppableId &&
        source.index !== destination.index
      ) {
        const swapData = data.map((list) => {
          if (list.id === destination?.droppableId) {
            const cardList = list.cardList;
            const sourceData = cardList.splice(source.index, 1);
            cardList.splice(destination.index, 0, sourceData[0]);
            return {
              ...list,
              cardList: cardList,
            };
          }
          return list;
        });
        setData(swapData);
      } else if (source.droppableId !== destination.droppableId) {
        let sourceData = [];
        const swapData = data?.map((list) => {
          if (list.id === source.droppableId) {
            const cardList = list.cardList;
            sourceData = cardList.splice(source.index, 1);
            return {
              ...list,
              cardList: cardList,
            };
          }
          return list;
        });

        const updatedData = swapData?.map((list) => {
          if (list.id === destination.droppableId) {
            const cardList = list.cardList;
            cardList.splice(destination.index, 0, sourceData[0]);
            return {
              ...list,
              cardList: cardList,
            };
          }
          return list;
        });
        setData(updatedData);
      }
    } else {
      return;
    }
  };

  return (
    <>
      <Header name="Trello" />
      <div className="p-4 flex gap-4 flex-wrap">
        {
          <DragDropContext onDragEnd={handleDragEnd}>
            {data &&
              data?.map((item, index) => {
                return (
                  <div key={index}>
                    <Card title={item} setData={setData} data={data} />
                  </div>
                );
              })}
          </DragDropContext>
        }
        {!showMiniCard && (
          <button
            className="w-[200px] h-[40px] flex items-center justify-center bg-[#dfeadf] hover:bg-[#bfc5bf] rounded"
            onClick={() => setShowMiniCard(!showMiniCard)}
          >
            {"Add Another List"}
          </button>
        )}
        {showMiniCard && (
          <div className="bg-black flex flex-col w-[200px] p-3 rounded-xl max-h-24">
            <div className="bg-black flex flex-col gap-4">
              <input
                id={"miniCard"}
                type={"text"}
                value={title}
                onChange={(e) => {
                  setTitle(e.target.value);
                }}
                className="text-sm w-42 font-semibold rounded px-2 py-1 text-white bg-black"
                autoFocus
                placeholder="Enter a list title..."
              />
              <button
                className="bg-[#84B8FE] w-20 p-1 rounded-lg"
                onClick={() => {
                  setList([...list, title]);
                  setShowMiniCard(!showMiniCard);
                  setTitle("");
                  const id = generateUniqueAlphabet();
                  setData([
                    ...data,
                    {
                      title,
                      id,
                      cardList: [],
                    },
                  ]);
                }}
              >
                Add list
              </button>
            </div>
          </div>
        )}
      </div>
    </>
  );
};

export default App;
