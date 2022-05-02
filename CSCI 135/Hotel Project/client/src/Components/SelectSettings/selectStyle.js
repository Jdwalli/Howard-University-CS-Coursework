export const selectStyle = {
    control: (base, state) => ({
      ...base,
      borderRadius: state.isFocused ? "3px 3px 0 0" : 3,
      borderColor: state.isFocused ? "yellow" : "green",
      boxShadow: state.isFocused ? null : null,
      "&:hover": {
      borderColor: state.isFocused ? "red" : "blue"
      }
    }),
    menu: (base) => ({
      ...base,
      background: "hsla(240, 10%, 18%, 0.9)",
      borderRadius: 0,
      marginTop: 0
    }),
    menuList: (base) => ({
      ...base,
      padding: 0
    })
  };      
  
  